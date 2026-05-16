def odd_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield True
if __name__ == '__main__':
    print(list(odd_generator(1, 10)))
    print(list(odd_generator(2, 8)))
    print(list(odd_generator(10, 12)))