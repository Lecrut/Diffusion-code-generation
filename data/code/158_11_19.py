START = 2
END = 100

def even_numbers():
    for i in range(START, END + 1):
        if i % 2 == 0:
            yield i

if __name__ == '__main__':
    for number in even_numbers():
        print(number)