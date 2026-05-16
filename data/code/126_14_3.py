def check_ten_generator(n):
    if n == 10:
        yield True
    else:
        yield False
if __name__ == '__main__':
    for i in [5, 10, 15, 10, 20, 100]:
        print(f"Input: {i}, Result: {next(check_ten_generator(i))}")