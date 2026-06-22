ODD_THRESHOLD = 1

def is_odd(n):
    return n % ODD_THRESHOLD != 0

if __name__ == '__main__':
    test_values = [7, -8, 9, 10, 0, -1, 2]
    for value in test_values:
        print(f"{value} is odd: {is_odd(value)}")