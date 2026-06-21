class AscendingComparator:
    def __init__(self, nums):
        self.nums = nums

    def compare_adjacent(self):
        return [self.nums[i] < self.nums[i + 1] for i in range(len(self.nums) - 1)]

if __name__ == '__main__':
    sample_values = [5, 7, 6, 8, 9]
    comparator = AscendingComparator(sample_values)
    result = comparator.compare_adjacent()
    print(result)