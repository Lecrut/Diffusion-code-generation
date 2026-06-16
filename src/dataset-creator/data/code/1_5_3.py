def check_positive(iterable):
    return any(x > 0 for x in iterable)
if __name__ == '__main__':
    print(check_positive([1, -2, 3]))
    print(check_positive([-5, -10]))
    print(check_positive([]))