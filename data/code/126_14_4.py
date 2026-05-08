def check_ten(n):
    if n == 10:
        yield True
    else:
        yield False
if __name__ == '__main__':
    generator1 = check_ten(10)
    print(list(generator1))
    generator2 = check_ten(5)
    print(list(generator2))
    generator3 = check_ten(20)
    print(list(generator3))