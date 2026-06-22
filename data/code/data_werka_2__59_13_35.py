class MiddleValueFinder:
    def __init__(self, nums):
        if not nums:
            raise ValueError("The list cannot be empty")
        self.nums = nums

    def find_middle_value(self):
        return self.quickselect(0, len(self.nums) - 1)

    def partition(self, low, high):
        pivot = self.nums[high]
        i = low
        for j in range(low, high):
            if self.nums[j] < pivot:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                i += 1
        self.nums[i], self.nums[high] = self.nums[high], self.nums[i]
        return i

    def quickselect(self, low, high):
        if low == high:
            return self.nums[low]

        pivot_index = self.partition(low, high)

        if pivot_index == len(self.nums) // 2:
            return self.nums[pivot_index]
        elif pivot_index < len(self.nums) // 2:
            return self.quickselect(pivot_index + 1, high)
        else:
            return self.quickselect(low, pivot_index - 1)

if __name__ == '__main__':
    sample_values = [7, 3, 5, 9, 1, 6]
    finder = MiddleValueFinder(sample_values)
    middle_value = finder.find_middle_value()
    print(middle_value)