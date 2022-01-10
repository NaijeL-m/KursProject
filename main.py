# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def ya_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_link_ya(self,adres_disk_file):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.ya_headers()
        params = {"path":adres_disk_file, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def papka(self, nazvanie):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.ya_headers()
        params = {"path": "test/" + str(nazvanie)}
        response = requests.put(url, headers=headers, params=params)
        return response.json()

    def upload(self, file_name, path):
        href = self.get_link_ya(adres_disk_file="test/test/"+path+file_name).get("href", "")
        print(href)
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        return response.status_code
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать

    def upload_link(self, link, path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.ya_headers()
        params = {"path": path, "url": link}
        response = requests.post(url, headers=headers, params=params)
        return response.json()

    def upload_vk_friends_photo(self,id_vk):
        result=[]
        i=0
        self.papka(id_vk)
        spisok_friends=requests.get('https://api.vk.com/method/friends.get?user_id='+str(id_vk)+'&fields=bdate&access_token=c95a7f4ec95a7f4ec95a7f4e00c920c5b9cc95ac95a7f4ea88f30626a14b98bdd430a77&v=5.131')
        for friend in spisok_friends.json()['response']['items']:
            photoes = requests.get('https://api.vk.com/method/photos.get?owner_id=' + str(friend['id']) + '&album_id=profile&extended=1&access_token=c95a7f4ec95a7f4ec95a7f4e00c920c5b9cc95ac95a7f4ea88f30626a14b98bdd430a77&v=5.131')
            if photoes.json().get('response') != None and photoes.json().get('error') == None:
                if photoes.json()['response']['count'] > 0:
                    i+=1
                    file_url = photoes.json()['response']['items'][0]['sizes'][-1]['url']
                    file_name = photoes.json()['response']['items'][0]['likes']['count']
                    file_size = photoes.json()['response']['items'][0]['sizes'][-1]['type']
                    self.upload_link(file_url,"test/"+str(id_vk)+"/"+str(file_name)+".jpg")
                    result.append({'file_name': str(file_name)+".jpg", 'size': file_size})
        return result

def  vk_friends_photo_upload(id_vk):
    res = requests.get('https://api.vk.com/method/friends.get?user_id='+str(id_vk)+'&fields=bdate&access_token=c95a7f4ec95a7f4ec95a7f4e00c920c5b9cc95ac95a7f4ea88f30626a14b98bdd430a77&v=5.131')
    for fr in res.json()['response']['items']:
        print(fr['id'])
        photoes=requests.get('https://api.vk.com/method/photos.get?owner_id='+str(fr['id'])+'&album_id=profile&access_token=c95a7f4ec95a7f4ec95a7f4e00c920c5b9cc95ac95a7f4ea88f30626a14b98bdd430a77&v=5.131')
        if photoes.json().get('response')!=None and photoes.json().get('error')==None:
            if photoes.json()['response']['count']>0:
                file=requests.get(photoes.json()['response']['items'][0]['sizes'][0]['url'])
                with open(str(fr['id'])+'.jpg','ab') as f:
                    f.write(file.content)
                path_to_file = str(fr['id'])+'.jpg'
                token = "AQAAAABXhZfHAADLW0t9sCIlwkPlnOFc_Q_3CBM"
                uploader = YaUploader(token)
                result = uploader.upload(path_to_file,'')
                print(result)

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file_on_computer = "test.txt"
    token = "AQAAAABXhZfHAADLW0t9sCIlwkPlnOFc_Q_3CBM"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file_on_computer, '')
    #result = uploader.get_link_ya("test/net").get("href", "")
    print(result)
    print(uploader.upload_vk_friends_photo(552934290))








hello=True