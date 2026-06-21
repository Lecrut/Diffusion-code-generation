class NumberFilter:
    @staticmethod
    def filter_evens(numbers):
        return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    number_filter = NumberFilter()
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = number_filter.filter_evens(sample_numbers)
    print(even_numbers)