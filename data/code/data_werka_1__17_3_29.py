class EvenNumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_even(self):
        return [num for num in self.numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_filter = EvenNumberFilter(sample_numbers)
    even_numbers = even_filter.filter_even()
    print("Even numbers:", even_numbers)