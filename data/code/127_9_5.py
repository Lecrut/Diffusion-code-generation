def is_odd(num):
    return num & 1 == 1
if __name__ == '__main__':
    test_values = [3, 5, 8, 21]
    for value in test_values:
        print(f'{value} is odd: {is_odd(value)}')