class NumberValidator:
    REQUIRED_COUNT = 3
    DIVISOR = 2

    @staticmethod
    def is_valid_number(num):
        return num > 0 and num % NumberValidator.DIVISOR == 0

    @staticmethod
    def check_numbers(numbers):
        valid_count = 0
        for num in numbers:
            if NumberValidator.is_valid_number(num):
                valid_count += 1
        return valid_count >= NumberValidator.REQUIRED_COUNT

if __name__ == '__main__':
    test_data = [2, 4, 6, -1, -2, 3]
    result = NumberValidator.check_numbers(test_data)
    print(result)