def check_even_odd(number):
    return number & 1 == 0

if __name__ == '__main__':
    test_numbers = [2, 7, 14, -3]
    for num in test_numbers:
        result = check_even_odd(num)
        print(f"Number: {num}, Even: {result}")