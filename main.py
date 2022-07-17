import math
import threading
import time
import requests

# Задание 1

start = time.time()


class UrlThread(threading.Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        requests.get(self.url)


th1 = UrlThread('https://google.com/')
th2 = UrlThread('https://google.com/')
th3 = UrlThread('https://google.com/')

th1.start()
th2.start()
th3.start()

url = time.time()-start
print(f'Время выполнения программы (запрос GET, на потоках) {url}')

start = time.time()


def without_threads():
    requests.get('https://google.com/')
    requests.get('https://google.com/')
    requests.get('https://google.com/')


w_url = time.time()-start
print(f'Время выполнения программы (запрос GET) {w_url}')

# Задание 2


start = time.time()


class MathThread(threading.Thread):

    def __init__(self, base_of_degree, exponent):
        super().__init__()
        self.base_of_degree = base_of_degree
        self.exponent = exponent

    def run(self):
        return self.base_of_degree ** self.exponent


th1 = MathThread(5, 78456)
th2 = MathThread(8, 3456)
th3 = MathThread(3, 667890)

th1.start()
th2.start()
th3.start()

math = time.time()-start
print(f'Время выполнения программы (c вычислением степени, на потоках): {time.time()- start}')
start = time.time()


def math_without_threads():
    s = 5**78456
    s = 8**3456
    s = 3**667890


w_math = time.time()-start
print(f'Время выполнения программы (c вычислением степени): {w_math}')

"""В обоих случаях разница во времени значительна -- стоит использовать потоки"""


