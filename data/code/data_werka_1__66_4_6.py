class IncreasingChecker:
    @staticmethod
    def is_strictly_increasing(numbers):
        return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_values = [3.5, 4.2, 5.0, 6.1, 7.8]
    result = IncreasingChecker.is_strictly_increasing(sample_values)
    print(result)