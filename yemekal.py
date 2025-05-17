from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
username=int(input("ogrenci no: "))
password=(input("sifre :"))


driver.get('https://kimlik.ege.edu.tr/Identity/Account/Login?ReturnUrl=%2F')
userbox= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
userbox.send_keys(username)
passbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password")))

passbox.send_keys(password)
giris = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.ID, "login-submit"))

)
giris.click()
time.sleep(5)
yemekbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='modal-opener']//strong[text()='Yemekhane Sistemi']"))
)
yemekbox.click()

ilcebox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='İlçe Yemekhaneleri']"))
)
ilcebox.click()
handles = driver.window_handles
driver.switch_to.window(handles[1])

kapatbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#myModal > div > div > div.modal-footer > button"))

)
kapatbox.click()

time.sleep(5)
driver.get("https://sksilceyemek.ege.edu.tr/YemekRezervasyon.aspx?o=O&Yemekhane=16&Vejeteryan=Hayir")

days = driver.find_elements(By.XPATH, "//td[contains(@style, 'font-size:large;')]")
day_list = []


for index, day in enumerate(days, start=1):
    day_text = day.text.strip()
    day_list.append(f"{index}- {day_text}")
    print(f"{index}- {day_text}")



selected_days = input("Seçmek istediğiniz günlerin numaralarını giriniz (örneğin: 1 3 5): ")
selected_days = [int(day) - 1 for day in selected_days.split()]
time.sleep(5)

for i in selected_days:
    day_checkbox = driver.find_element(By.ID, f"ContentPlaceHolder1_rptKahvalti_checkYemeklerKahvalti_{i}")
    time.sleep(0.3)
    day_checkbox.click()



sepet=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"#ContentPlaceHolder1_btnSepetEkle"))
)
sepet.click()
print("sepete ekleme başarılı")

driver.get("https://sksilceyemek.ege.edu.tr/Sepetim.aspx")

satin=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"#ContentPlaceHolder1_btnSatinAl"))
)
satin.click()
print("ödeme başarılya yapıldı")
time.sleep(3)
