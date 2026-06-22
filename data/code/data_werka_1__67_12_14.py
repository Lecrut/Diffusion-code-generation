class MaxProductFinder:

    def __init__(self, nums):
        self.nums = nums
        self.max1 = max2 = float('-inf')
        self.min1 = min2 = float('inf')
        for num in nums:
            if num > self.max1:
                self.max2 = self.max1
                self.max1 = num
            elif num > self.max2:
                self.max2 = num
            if num < self.min1:
                self.min2 = self.min1
                self.min1 = num
            elif num < self.min2:
                self.min2 = num

    def find_max_product_pair(self):
        return max(self.max1 * self.max2, self.min1 * self.min2)
if __name__ == '__main__':
    nums = [3, 6, -2, -5, 7, 3]
    finder = MaxProductFinder(nums)
    result = finder.find_max_product_pair()
    print(result)
    nums2 = [-10, -20, 5, 1]
    finder2 = MaxProductFinder(nums2)
    result2 = finder2.find_max_product_pair()
    print(result2)