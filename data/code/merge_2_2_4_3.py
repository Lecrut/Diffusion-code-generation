def is_positive(value):
    return value > 0
if __name__ == '__main__':
    print(is_positive(5))
    print(is_positive(-3))
    print(is_positive(0))
    print(is_positive(float('inf')))
    print(is_positive(float('-inf')))