def determine_larger(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2
if __name__ == '__main__':
    print(determine_larger(10, 5))
    print(determine_larger(3.14, 2.71))
    print(determine_larger(-5, -10))
    print(determine_larger(100, 200))
    print(determine_larger(42.5, 42.5))