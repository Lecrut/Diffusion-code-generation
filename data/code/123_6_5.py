DIGIT_MAP = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def sum_of_digits(n):
    return sum(DIGIT_MAP[digit] for digit in str(abs(n)))

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(-9876))