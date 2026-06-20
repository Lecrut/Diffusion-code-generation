def check_range(value):
    if isinstance(value, int) and 1 <= value <= 10:
        return True
    return False
if __name__ == '__main__':
    print(check_range(5))
    print(check_range(0))
    print(check_range(11))