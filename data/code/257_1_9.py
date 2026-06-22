class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_difference(self):
        if not self.numbers:
            raise ValueError("The tuple must contain at least one number.")
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.9)
    analyzer = NumberAnalyzer(sample_values)
    difference = analyzer.find_difference()
    print("The difference between the largest and smallest numbers is:", difference)