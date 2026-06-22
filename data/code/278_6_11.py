class FloatFormatter:
    def format_numbers(self, numbers):
        for number in numbers:
            print(f"{number:.2f}")

if __name__ == '__main__':
    formatter = FloatFormatter()
    sample_numbers = [3.14159, 2.71828, 0.00123, 100.0]
    formatter.format_numbers(sample_numbers)