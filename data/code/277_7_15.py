class DigitCounter:
    @staticmethod
    def count_digits(number):
        if number == 0:
            return 1
        digits = 0
        abs_number = abs(number)
        while abs_number > 0:
            abs_number //= 10
            digits += 1
        return digits

if __name__ == '__main__':
    sample_numbers = [0, 5, 12345, -67890]
    for number in sample_numbers:
        result = DigitCounter.count_digits(number)
        print(f"Number of digits in {number}: {result}")