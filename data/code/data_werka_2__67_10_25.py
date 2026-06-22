class TwoSumFinder:
    DEFAULT_ARRAY = [10, 20, 30, 40, 50, 60]
    DEFAULT_TARGET = 90

    @staticmethod
    def find_pair(arr, target):
        left = 0
        right = len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return (arr[left], arr[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        raise ValueError("No two elements sum up to the target value")

if __name__ == '__main__':
    sample_array = [5, 7, 9, 12, 14, 18]
    target_value = 26
    finder = TwoSumFinder()
    result = finder.find_pair(sample_array, target_value)
    print(result)