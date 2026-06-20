def is_even(number):
    return number & 1 == 0

if __name__ == '__main__':
    test_numbers = [24, 57, -8, 32, -9]
    for num in test_numbers:
        print(f"Number {num} is even: {is_even(num)}")