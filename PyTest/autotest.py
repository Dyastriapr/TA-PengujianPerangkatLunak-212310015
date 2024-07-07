from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # Buka halaman OrangeHRM
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Tunggu hingga elemen input username muncul
    username_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))
    )

    # Masukkan kredensial dan klik tombol login
    username_box.send_keys("Admin")
    password_box.send_keys("admin123")
    login_button.click()

    # Tunggu hingga elemen dashboard muncul
    dashboard = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "welcome"))
    )

    # Navigasi ke halaman Add Employee
    pim_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.oxd-main-menu-item[href*='viewPimModule']")
        )
    )
    pim_menu.click()

    # Tunggu hingga menu Add Employee muncul
    add_employee_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.oxd-main-menu-item[href*='addEmployee']")
        )
    )
    add_employee_button.click()

    # Isi form Add Employee
    first_name_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    )
    last_name_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "lastName"))
    )
    employee_id_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input.oxd-input[name='employeeId']")
        )
    )

    first_name_box.send_keys("John")
    last_name_box.send_keys("Doe")
    employee_id_box.clear()
    employee_id_box.send_keys("1234")

    save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    save_button.click()

    # Verifikasi bahwa karyawan baru berhasil ditambahkan
    personal_details_header = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']"))
    )
    assert (
        personal_details_header.is_displayed()
    ), "Add Employee gagal atau elemen Personal Details tidak ditemukan"

    print(
        "Test passed: Karyawan baru berhasil ditambahkan dan elemen Personal Details ditemukan."
    )

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Tutup browser
    driver.quit()
