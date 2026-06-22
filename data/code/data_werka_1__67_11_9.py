class TwoSumSolver:
    def __init__(self, sorted_array):
        self.sorted_array = sorted_array

    @staticmethod
    def find_pair_with_sum(sorted_array, target):
        left, right = 0, len(sorted_array) - 1
        while left < right:
            current_sum = sorted_array[left] + sorted_array[right]
            if current_sum == target:
                return (sorted_array[left], sorted_array[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None

if __name__ == '__main__':
    sample_array = [1, 3, 5, 7, 9, 11]
    target_value = 10
    solver = TwoSumSolver(sample_array)
    result = solver.find_pair_with_sum(sample_array, target_value)
    print(result)