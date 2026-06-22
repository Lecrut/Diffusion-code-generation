class ArrayStatistics:
    DEFAULT_ARRAY = [4, 8, 12, 16]

    @staticmethod
    def calculate_mean(arr):
        total = sum(arr)
        count = len(arr)
        average = total / count
        return average

if __name__ == '__main__':
    sample_array = ArrayStatistics.DEFAULT_ARRAY
    result = ArrayStatistics.calculate_mean(sample_array)
    print(result)