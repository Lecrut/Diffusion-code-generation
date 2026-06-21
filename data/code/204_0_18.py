import statistics

class MedianFinder:
    @staticmethod
    def find_middle_value(numbers):
        if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
            raise ValueError("Input must be a list of numbers")
        return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    try:
        print(MedianFinder.find_middle_value(sample_values))
    except ValueError as e:
        print(e)