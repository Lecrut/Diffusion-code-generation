class NumberFilter:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @classmethod
    def filter_evens(cls, numbers):
        return [num for num in numbers if cls.is_even(num)]

if __name__ == '__main__':
    sample_values = [15, 22, 37, 48, 51, 64, 79, 80, 93, 100]
    even_numbers = NumberFilter.filter_evens(sample_values)
    print(even_numbers)