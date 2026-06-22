class MaxFinder:
    @staticmethod
    def find_largest(numbers):
        return max((num for num in numbers if isinstance(num, (int, float))), default=None)

if __name__ == '__main__':
    sample_numbers = [3.5, 10, 2, 7, 8, 15, -1]
    print(MaxFinder.find_largest(sample_numbers))