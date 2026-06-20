def is_odd(num):
    return num & 1

class OddNumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.odd_count = sum(is_odd(num) for num in self.numbers)

    def get_odd_count(self):
        return self.odd_count

    def is_odd_count_even(self):
        return self.odd_count % 2 == 0

if __name__ == '__main__':
    analyzer = OddNumberAnalyzer([1, 2, 3, 4, 5, 6])
    print(analyzer.get_odd_count())
    print(analyzer.is_odd_count_even())