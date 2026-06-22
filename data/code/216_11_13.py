class MedianCalculator:
    @staticmethod
    def find_median(data):
        n = len(data)
        if n == 0:
            return None
        sorted_data = sorted(data)
        middle_index = n // 2
        if n % 2 == 1:
            return sorted_data[middle_index]
        else:
            lower_middle_index = middle_index - 1
            median = (sorted_data[lower_middle_index] + sorted_data[middle_index]) / 2
            return median

if __name__ == '__main__':
    lists = [[4, 7, 2, 5, 8], [1, 3, 2], [5, 2, 8, 1, 9], [10], []]
    for lst in lists:
        print(f"Median of {lst} is: {MedianCalculator.find_median(lst)}")