class IntegerListAnalyzer:
    def __init__(self, integers):
        self.integers = integers

    def find_highest_value(self):
        if not self.integers:
            raise ValueError("The list is empty")
        return max(self.integers)

if __name__ == '__main__':
    analyzer = IntegerListAnalyzer([10, 5, 20, 8, 15])
    try:
        highest_value = analyzer.find_highest_value()
        print(highest_value)
    except ValueError as e:
        print(e)