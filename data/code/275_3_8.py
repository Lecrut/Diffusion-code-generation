class NumberAnalyzer:
    def __init__(self, numbers):
        self._numbers = numbers
    
    def count_even_numbers(self):
        return sum(1 for num in self._numbers if num % 2 == 0)

if __name__ == '__main__':
    analyzer = NumberAnalyzer([10, 23, 45, 68, 70])
    result = analyzer.count_even_numbers()
    print(result)