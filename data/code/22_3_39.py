class NumberFilter:
    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    @classmethod
    def filter_odd_numbers(cls, numbers):
        return [num for num in numbers if cls.is_odd(num)]

if __name__ == '__main__':
    sample_values = [15, 22, 37, 48, 59, 64, 73, 80, 91, 102]
    odd_numbers = NumberFilter.filter_odd_numbers(sample_values)
    print(odd_numbers)