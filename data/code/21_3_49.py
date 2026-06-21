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
    sample_values = [12, 34, 56, 78, 90, 11, 23, 35]
    result = sort_and_count(sample_values)
    print(result)
    another_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    another_result = sort_and_count(another_sample)
    print(another_result)