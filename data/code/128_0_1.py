def check_negativity(number):
    if number < 0:
        return True
    else:
        return False
if __name__ == '__main__':
    test_numbers = [10, -5, 0, -100, 3.14]
    for num in test_numbers:
        result = check_negativity(num)
        print(f"Testing number: {num}, Is negative: {result}")