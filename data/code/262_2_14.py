class MinMaxFinder:
    @staticmethod
    def find_min_max(numbers):
        if not numbers:
            return None, None
        minimum = min(numbers)
        maximum = max(numbers)
        return minimum, maximum

if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 3, 15]
    min1, max1 = MinMaxFinder.find_min_max(sample_data1)
    print(f"Data set 1: {sample_data1}")
    print(f"Minimum: {min1}, Maximum: {max1}")