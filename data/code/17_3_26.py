class EvenNumberFilter:
    EVEN = 0

    @staticmethod
    def is_even(number):
        return number % 2 == EvenNumberFilter.EVEN

    @staticmethod
    def filter_evens(numbers):
        return [num for num in numbers if EvenNumberFilter.is_even(num)]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = EvenNumberFilter.filter_evens(sample_values)
    print(even_numbers)