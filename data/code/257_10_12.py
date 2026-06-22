class ListAnalyzer:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def calculate_difference(self) -> int:
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    sample_list = [10, 4, 25, 7, 5]
    analyzer = ListAnalyzer(sample_list)
    result = analyzer.calculate_difference()
    print(result)