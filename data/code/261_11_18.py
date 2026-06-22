import statistics

class MedianCalculator:
    @staticmethod
    def calculate_median(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return statistics.median(data)

if __name__ == '__main__':
    calculator = MedianCalculator()
    print(f"Median of [1, 3, 5, 7, 9]: {calculator.calculate_median([1, 3, 5, 7, 9])}")
    print(f"Median of [4, 1, 8, 3, 6, 2]: {calculator.calculate_median([4, 1, 8, 3, 6, 2])}")