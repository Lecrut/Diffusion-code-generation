def check_ten_generator(n):
    if n == 10:
        yield True
    else:
        yield False
if __name__ == '__main__':
    for number in [5, 10, 15, 10, 20, 100]:
        for result in check_ten_generator(number):
            print(result)