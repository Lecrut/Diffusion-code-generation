class MaxFinder:
    @staticmethod
    def find_largest(numbers):
        return max((num for num in numbers if isinstance(num, (int, float))), default=None)

if __name__ == '__main__':
    sample_numbers = [3.14, 2.718, 1.618, 0.577, 10**9]
    print(MaxFinder.find_largest(sample_numbers))