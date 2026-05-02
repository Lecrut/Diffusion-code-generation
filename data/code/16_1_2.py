def is_positive(number):
    return number > 0
if __name__ == '__main__':
    print(is_positive(5))
    print(is_positive(-1))
    print(is_positive(0))
    print(is_positive(1.0000000000000002))
    print(is_positive(-0.0000000000000001))