def is_negative(number):
    return number < 0

if __name__ == '__main__':
    test_numbers = [-10, 5, -3.14, 0]
    for num in test_numbers:
        print(f"Testing number: {num}, Is negative: {is_negative(num)}")