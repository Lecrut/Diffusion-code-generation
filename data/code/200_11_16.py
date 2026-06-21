def every_second_element():
    hard_coded_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for index in range(1, len(hard_coded_list), 2):
        yield hard_coded_list[index]

if __name__ == '__main__':
    gen = every_second_element()
    print(next(gen))
    print(next(gen))
    print(next(gen))