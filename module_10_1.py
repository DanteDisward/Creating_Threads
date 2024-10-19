from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово №{i + 1}\n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    return True


# ============================ Функции ======================================
time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

# ============================== Потоки ======================================
time_start = datetime.now()
example5 = Thread(target=write_words, args=(10, 'example5.txt'))
example6 = Thread(target=write_words, args=(30, 'example6.txt'))
example7 = Thread(target=write_words, args=(200, 'example7.txt'))
example8 = Thread(target=write_words, args=(100, 'example8.txt'))

example5.start()
example6.start()
example7.start()
example8.start()

example5.join()
example6.join()
example7.join()
example8.join()

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)
