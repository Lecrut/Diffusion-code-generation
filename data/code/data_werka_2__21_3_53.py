class NumberAnalyzer:

    def __init__(self, numbers):
        self.numbers = numbers

    def sort_numbers(self):
        return sorted(self.numbers)

    def count_evens(self):
        return sum((1 for num in self.numbers if num % 2 == 0))

def sort_and_count(numbers):
    analyzer = NumberAnalyzer(numbers)
    sorted_numbers = analyzer.sort_numbers()
    even_count = analyzer.count_evens()
    return (sorted_numbers, even_count)
if __name__ == '__main__':
    sample_values = [12, 34, 56, 78, 90, 23, 45, 67]
    result = sort_and_count(sample_values)
    print(result)
    analyzer_instance = NumberAnalyzer(sample_values)
    print('Sorted Numbers:', analyzer_instance.sort_numbers())
    print('Even Count:', analyzer_instance.count_evens())