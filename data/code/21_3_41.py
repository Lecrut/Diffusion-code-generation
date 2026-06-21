class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def sort_numbers(self):
        return sorted(self.numbers)

    def count_evens(self):
        return sum(1 for num in self.numbers if num % 2 == 0)

def sort_and_count(numbers):
    processor = NumberProcessor(numbers)
    sorted_numbers = processor.sort_numbers()
    even_count = processor.count_evens()
    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_values = [15, 3, 8, 6, 2, 7, 4, 1]
    result = sort_and_count(sample_values)
    print(result)