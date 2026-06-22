def check_or_greater_than_ten(a, b):
    return a > 10 or b > 10

if __name__ == '__main__':
    x = 12
    y = 5
    result = check_or_greater_than_ten(x, y)
    print(result)