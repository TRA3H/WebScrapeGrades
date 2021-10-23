import requests
from bs4 import BeautifulSoup
cookies = {
    'JSESSIONID': 'node0bylg11etb77h1bn7znffwvw2z2556888.node0',
    'BIGipServershibboleth.fullerton.edu_pool_http': '1822660489.18719.0000',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = (
    ('execution', 'e1s1'),
)

login_data = {
    'j_username' : "username", #Where my username goes
    'j_password' : "password" #Where my password goes
}

with requests.Session() as s:
    url = 'https://shibboleth.fullerton.edu/idp/profile/SAML2/Redirect/SSO'
    r = s.get(url, headers=headers, params=params, cookies=cookies)
    soup = BeautifulSoup(r.content, 'html5lib')
    login_data['LoginTextBox'] = soup.find('input' , attrs={'name': 'j_username'})['value']

    r = s.post(url, data = login_data, headers=headers, params=params, cookies=cookies)
    print(r.content)



#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://shibboleth.fullerton.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s1', headers=headers, cookies=cookies)