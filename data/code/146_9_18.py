class MaxSubarrayFinder:
    def __init__(self, arr):
        self.arr = arr

    def find_max_subarray_sum(self):
        max_current = max_global = self.arr[0]
        for num in self.arr[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global

if __name__ == '__main__':
    finder = MaxSubarrayFinder([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(finder.find_max_subarray_sum())