DIGIT_MAPPING = {
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

def sum_of_digits(n):
    return sum([DIGIT_MAPPING[d] for d in str(n)])

if __name__ == '__main__':
    test_values = [1984, 777, 50505]
    for value in test_values:
        print(sum_of_digits(value))