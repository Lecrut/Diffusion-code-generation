class FloatFormatter:
    DECIMAL_PLACES = 2

    @staticmethod
    def format_float(number):
        return f"{number:.{FloatFormatter.DECIMAL_PLACES}f}"

if __name__ == '__main__':
    sample_numbers = [3.14159, 2.71828, 0.00123, 100.0]
    for number in sample_numbers:
        print(FloatFormatter.format_float(number))