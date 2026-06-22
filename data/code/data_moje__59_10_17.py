DIGIT_VALUES = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def sum_digits_arithmetic(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    s = str(n)
    total = 0
    for char in s:
        total += DIGIT_VALUES[char]
    return total

if __name__ == '__main__':
    n = 87329104
    val = sum_digits_arithmetic(n)
    print(val)
    n2 = 0
    val2 = sum_digits_arithmetic(n2)
    print(val2)
    n3 = 1000000
    val3 = sum_digits_arithmetic(n3)
    print(val3)