class NumberUtils:
    @staticmethod
    def is_negative(number):
        return number < 0

if __name__ == '__main__':
    test_number = -10
    result = NumberUtils.is_negative(test_number)
    print(f"The test number is: {test_number}")
    print(f"Is the number negative? {result}")