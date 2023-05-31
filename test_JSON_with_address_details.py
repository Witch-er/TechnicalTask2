import pytest
import requests
data_header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",'Content-Type': 'application/json; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=20', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'OPTIONS,GET'}
@pytest.mark.parametrize('address', [("Touch of Home Bakery"), ("Touch of Home Bakery1"), ("")])
def test_adress_search(address):
    r = requests.get("https://nominatim.openstreetmap.org/?addressdetails=1&q="+str(address)+"&format=json&limit=1", headers=data_header, verify=False)
    assert r.status_code == 200
    print()
    print(r.json())
