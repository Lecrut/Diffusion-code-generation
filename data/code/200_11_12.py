EVEN_INDEX = 0

def every_second_element():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index in range(EVEN_INDEX, len(data), 2):
        yield data[index]

if __name__ == '__main__':
    gen = every_second_element()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))