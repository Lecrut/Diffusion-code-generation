def find_median(nums):
    nums.sort()
    N = len(nums)
    if N % 2 == 1:
        return nums[N // 2]
    else:
        floor_index = N // 2 - 1
        ceiling_index = N // 2
        return (nums[floor_index] + nums[ceiling_index]) / 2

class MedianCalculator:
    def __init__(self, data):
        self.data = data
    
    def calculate_median(self):
        return find_median(self.data)

if __name__ == '__main__':
    calculator_odd = MedianCalculator([3, 1, 4, 1, 5, 9, 2])
    print(f"Median of odd list: {calculator_odd.calculate_median()}")
    
    calculator_even = MedianCalculator([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Median of even list: {calculator_even.calculate_median()}")