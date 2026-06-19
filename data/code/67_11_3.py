class TwoSumFinder:
    def __init__(self, arr):
        if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
            raise ValueError("Input must be a list of integers.")
        self.arr = sorted(arr)

    def find_pair(self, target):
        left, right = 0, len(self.arr) - 1
        while left < right:
            current_sum = self.arr[left] + self.arr[right]
            if current_sum == target:
                return (self.arr[left], self.arr[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None

if __name__ == '__main__':
    sample_array = [3, 5, 7, 8, 10, 12]
    target_value = 15
    finder = TwoSumFinder(sample_array)
    result = finder.find_pair(target_value)
    print(result)