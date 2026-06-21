class NumberFilter:
    EVEN = 0

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    def filter_evens(self, numbers):
        return [num for num in numbers if self.is_even(num)]

if __name__ == '__main__':
    sample_values = [15, 22, 37, 48, 51, 64, 79, 80, 93, 100]
    number_filter = NumberFilter()
    even_numbers = number_filter.filter_evens(sample_values)
    print(even_numbers)