class AscendingComparer:
    @staticmethod
    def compare_adjacent_ascending(nums):
        return [nums[i] < nums[i + 1] for i in range(len(nums) - 1)]

if __name__ == '__main__':
    sample_values = [7, 8, 5, 9, 6]
    comparer = AscendingComparer()
    result = comparer.compare_adjacent_ascending(sample_values)
    print(result)