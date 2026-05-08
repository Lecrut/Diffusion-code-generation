def check_ten_generator(n):
    if n == 10:
        yield True
    else:
        yield False
if __name__ == '__main__':
    print(list(check_ten_generator(10)))
    print(list(check_ten_generator(5)))
    print(list(check_ten_generator(20)))
    print(list(check_ten_generator(1000000)))