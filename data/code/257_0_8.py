class MaxMinDifference:
    @staticmethod
    def calculate_difference(numbers):
        if not numbers:
            return 0
        return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_list = [10, 3, 5, 2, 8]
    result = MaxMinDifference.calculate_difference(sample_list)
    print(result)