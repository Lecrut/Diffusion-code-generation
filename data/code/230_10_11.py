class EvenNumberFilter:
    def filter_evens(self, numbers):
        return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    even_filter = EvenNumberFilter()
    evens = even_filter.filter_evens(sample_numbers)
    print(evens)