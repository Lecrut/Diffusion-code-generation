def is_odd(num):
    return num & 1 == 1

if __name__ == '__main__':
    test_number = 29
    result = is_odd(test_number)
    print(result)