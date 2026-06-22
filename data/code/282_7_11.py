class RecursiveSumCalculator:
    @staticmethod
    def recursive_sum(numbers):
        if not numbers:
            return 0
        return numbers[0] + RecursiveSumCalculator.recursive_sum(numbers[1:])

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    result = RecursiveSumCalculator.recursive_sum(sample_sequence)
    print(result)