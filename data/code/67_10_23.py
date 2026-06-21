class TwoSumFinder:
    def __init__(self, arr):
        self.arr = arr

    def find_pair(self, target):
        left = 0
        right = len(self.arr) - 1
        while left < right:
            current_sum = self.arr[left] + self.arr[right]
            if current_sum == target:
                return (self.arr[left], self.arr[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        raise ValueError("No two elements sum up to the target value")

if __name__ == '__main__':
    sample_array = [2, 3, 5, 7, 8, 9]
    target_value = 14
    finder = TwoSumFinder(sample_array)
    result = finder.find_pair(target_value)
    print(result)