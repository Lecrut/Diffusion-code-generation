def even_numbers():
    START = 2
    END = 100
    STEP = 2
    for i in range(START, END + 1, STEP):
        yield i

if __name__ == '__main__':
    for number in even_numbers():
        print(number)