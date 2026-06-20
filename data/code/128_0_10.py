NEGATIVE_THRESHOLD = 0

def is_negative(number):
    return number < NEGATIVE_THRESHOLD

if __name__ == '__main__':
    test_numbers = [-1, 0, 5, -100, 3.14]
    for num in test_numbers:
        result = is_negative(num)
        print(f"Testing number: {num}, Is negative: {result}")