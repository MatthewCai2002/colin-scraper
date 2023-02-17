# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Constants definitions"""
import os
from dotenv import load_dotenv

load_dotenv()

STAFF_USERNAME = os.getenv('STAFF_USERNAME')
STAFF_PASSWORD = os.getenv('STAFF_PASSWORD')
ORACLE_USERNAME =  os.getenv('ORACLE_DB_USERNAME')
ORACLE_PASSWORD =  os.getenv('ORACLE_DB_PASSWORD')
ORACLE_DSN =  os.getenv('ORACLE_DB_DSN')
TEST_ORG = os.getenv('TEST_ORG_NUM')
INIT_START_DATE = os.getenv('DATE_RANGE_START')
INIT_END_DATE = os.getenv('DATE_RANGE_END')
FINAL_END_DATE = os.getenv('FINAL_END_DATE')

REGISTRY_SEARCH_URL = 'http://gaucho.bcgov:7777/corporateonline/colin/search/searchAction.do?action=setup&org.apache.struts.taglib.html.TOKEN=c2cbbb166a6e92f91d38f0dcf48bb866'
LOG_IN_URL = 'http://gaucho.bcgov:7777/corporateonline/colin/signon/start.do?action=login'

CONFIG_PATH = r'.\config'
DRIVER_PATH = r'.\chrome-web-driver\chromedriver.exe'
TEMP_BASE_PATH = r".\test-outputs"
UNWANTED_TAGS = ['MAIL', 'EMAIL']
