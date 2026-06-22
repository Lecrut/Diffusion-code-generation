class MiddleValueFinder:
    def __init__(self, nums):
        if not nums:
            raise ValueError("The list cannot be empty")
        self.nums = nums

    def find_middle_value(self):
        return self.quickselect(0, len(self.nums) - 1, len(self.nums) // 2)

    def partition(self, low, high):
        pivot = self.nums[high]
        i = low - 1
        for j in range(low, high):
            if self.nums[j] <= pivot:
                i += 1
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        self.nums[i + 1], self.nums[high] = self.nums[high], self.nums[i + 1]
        return i + 1

    def quickselect(self, low, high, k):
        if low == high:
            return self.nums[low]
        pivot_index = self.partition(low, high)
        if k == pivot_index:
            return self.nums[k]
        elif k < pivot_index:
            return self.quickselect(low, pivot_index - 1, k)
        else:
            return self.quickselect(pivot_index + 1, high, k)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2]
    finder = MiddleValueFinder(sample_values)
    middle_value = finder.find_middle_value()
    print(middle_value)