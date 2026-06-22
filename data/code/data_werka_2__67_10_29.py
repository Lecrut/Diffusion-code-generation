class TwoSumSolver:
    ARRAY_NOT_SORTED = "The array must be sorted to use this method."

    @staticmethod
    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    def __init__(self, arr):
        if not self.is_sorted(arr):
            raise ValueError(self.ARRAY_NOT_SORTED)
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
    sample_array = [1, 3, 5, 7, 9, 11]
    target_value = 16
    solver = TwoSumSolver(sample_array)
    result = solver.find_pair(target_value)
    print(result)