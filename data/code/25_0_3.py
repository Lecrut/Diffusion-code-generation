def check_for_zero(number):
    return number == 0
if __name__ == '__main__':
    test_numbers = [1, 0, -5, 100, 0.0]
    for num in test_numbers:
        result = check_for_zero(num)
        print(f"Is {num} zero? {result}")