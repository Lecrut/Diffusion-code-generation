def is_positive_and_less_than_100(value):
    return value > 0 and value < 100
if __name__ == '__main__':
    print(is_positive_and_less_than_100(50))
    print(is_positive_and_less_than_100(-10))
    print(is_positive_and_less_than_100(100))