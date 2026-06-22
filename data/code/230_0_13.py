class EvenNumberFilter:
    @staticmethod
    def filter_evens(numbers):
        return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = EvenNumberFilter.filter_evens(sample_numbers)
    print(even_numbers)