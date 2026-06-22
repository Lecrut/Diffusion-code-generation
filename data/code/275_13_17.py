class FilterEvenNumbers:
    MIN_VALUE = 10

    @staticmethod
    def is_even_and_greater_than_min(num):
        return num > FilterEvenNumbers.MIN_VALUE and num % 2 == 0

    @classmethod
    def filter_numbers(cls, numbers_set):
        return {num for num in numbers_set if cls.is_even_and_greater_than_min(num)}

if __name__ == '__main__':
    sample_numbers = {8, 15, 20, 7, 12}
    result = FilterEvenNumbers.filter_numbers(sample_numbers)
    print(result)