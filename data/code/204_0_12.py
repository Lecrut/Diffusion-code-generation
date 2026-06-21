import statistics

class MedianFinder:
    @staticmethod
    def find_middle_value(numbers):
        return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [7, 3, 5, 2, 9]
    print(MedianFinder.find_middle_value(sample_values))