class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = list(map(float, numbers.split()))

    def find_max(self):
        if not self.numbers:
            raise ValueError("Input string cannot be empty")
        max_value = self.numbers[0]
        for number in self.numbers[1:]:
            if number > max_value:
                max_value = number
        return max_value

if __name__ == '__main__':
    analyzer1 = NumberAnalyzer("3.14159 2.71828 1.61803")
    print(f"Max in '3.14159 2.71828 1.61803': {analyzer1.find_max()}")

    analyzer2 = NumberAnalyzer("-5.0 -10.5 -2.2")
    print(f"Max in '-5.0 -10.5 -2.2': {analyzer2.find_max()}")

    analyzer3 = NumberAnalyzer("0.0 0.0 0.0")
    print(f"Max in '0.0 0.0 0.0': {analyzer3.find_max()}")

    try:
        analyzer4 = NumberAnalyzer("")
        print(f"Max in '': {analyzer4.find_max()}")
    except ValueError as e:
        print(e)