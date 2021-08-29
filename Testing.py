import unittest
import requests

class Testing(unittest.TestCase):

    def test_statusCode(self):
        url2 = 'http://httpbin.org/headers'
        r = requests.get(url2)
        print("Status code:")
        print("\t *", r.status_code)

    def test_headers(self):
        url2 = 'http://httpbin.org/headers'
        headers = {'User-Agent': 'Mobile'}
        rh = requests.get(url2, headers=headers)
        print(rh.text)


if __name__ == '__main__':
    unittest.main()