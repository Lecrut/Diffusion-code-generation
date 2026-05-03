def check_for_zero(number):
    return number == 0
if __name__ == '__main__':
    test_numbers = [0, 5, -3, 0.0, 100]
    for num in test_numbers:
        result = check_for_zero(num)
        print(f"Is {num} zero? {result}")