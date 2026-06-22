class FilterNumbers:
    DIVISOR = 3

    @staticmethod
    def filter_divisible_by_three(numbers):
        return list(filter(lambda x: x % FilterNumbers.DIVISOR == 0, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = FilterNumbers.filter_divisible_by_three(sample_values)
    print(result)