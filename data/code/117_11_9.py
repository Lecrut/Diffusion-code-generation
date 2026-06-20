def abs_diff(a, b):
    return a if a > b else b

if __name__ == '__main__':
    print(abs_diff(10, 20))
    print(abs_diff(-5, -15))
    print(abs_diff(30, 30))