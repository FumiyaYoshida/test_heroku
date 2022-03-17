# Selenium
from selenium import webdriver
# ChromeDriverのバージョンを合わせるらしい
import chromedriver_binary
# from webdriver_manager.chrome import ChromeDriverManager
# ページが読み込まれるまで待機するモジュール
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# ChromeDriverのオプション用モジュール
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs

# ドライバーのパス指定
driver_path = '/app/.chromedriver/bin/chromedriver'
# driver_path = "./../chromedriver98"

# Headless Chromeをあらゆる環境で起動させるオプション
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')
options.add_argument('--headless')

#クローラーの起動
chrome_service = fs.Service(executable_path = driver_path)
driver = webdriver.Chrome(service = chrome_service, options = options)

# ページへアクセス
driver.get('https://info.finance.yahoo.co.jp/fx/')
# ページが読み込まれるまでの最大待機時間（10秒）
wait = WebDriverWait(driver, 10)
# ページが読み込まれるまで待機
wait.until(EC.presence_of_all_elements_located)

# ドル円を取得
element = driver.find_element_by_xpath('//span[@id="USDJPY_top_bid"]').get_attribute("textContent")
# ドル円を表示
print(element)

# ドライバーを終了させる
driver.close()
driver.quit()
