def every_second_element():
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, len(data), 2):
        yield data[i]

if __name__ == '__main__':
    gen = every_second_element()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))