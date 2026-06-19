class OddNumberFilter:
    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    @classmethod
    def filter_odds(cls, numbers):
        return [num for num in numbers if cls.is_odd(num)]

if __name__ == '__main__':
    sample_values = [10, 23, 45, 68, 77, 90]
    odd_numbers = OddNumberFilter.filter_odds(sample_values)
    print(odd_numbers)