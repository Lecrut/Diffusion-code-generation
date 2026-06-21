def is_even(number):
    EVEN_BIT_MASK = 1
    return (number & EVEN_BIT_MASK) == 0

if __name__ == '__main__':
    test_values = [2, 3, 0, -4, -5, 8, -9, 16, -17, 32]
    for value in test_values:
        result = is_even(value)
        print(f"{value} is even: {result}")