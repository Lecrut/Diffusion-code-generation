class NumberFilter:
    @staticmethod
    def filter_odd_numbers(numbers):
        return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [10, 15, 20, 25, 30, 35, 40, 45]
    odd_numbers = NumberFilter.filter_odd_numbers(sample_values)
    print(odd_numbers)