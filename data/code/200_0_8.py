class NumberFilter:
    @staticmethod
    def filter_even(numbers):
        return [n for n in numbers if n % 2 == 0]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    filtered_numbers = NumberFilter.filter_even(sample_numbers)
    print(filtered_numbers)