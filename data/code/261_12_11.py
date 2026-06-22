class MedianFinder:

    def find_median(self, numbers):
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n == 0:
            return None
        mid_index = n // 2
        if n % 2 == 1:
            return sorted_numbers[mid_index]
        else:
            return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
if __name__ == '__main__':
    finder = MedianFinder()
    sample1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sample2 = [7, 0, 8, 2, 1, 4, 3, 6, 5]
    print(finder.find_median(sample1))
    print(finder.find_median(sample2))