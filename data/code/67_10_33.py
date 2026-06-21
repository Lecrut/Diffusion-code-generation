class TwoSumSolver:
    def __init__(self, sorted_array):
        self.sorted_array = sorted_array

    @staticmethod
    def find_pair_with_sum(array, target):
        left_index = 0
        right_index = len(array) - 1
        while left_index < right_index:
            current_sum = array[left_index] + array[right_index]
            if current_sum == target:
                return (array[left_index], array[right_index])
            elif current_sum < target:
                left_index += 1
            else:
                right_index -= 1
        raise ValueError("No two elements sum up to the target value")

    def find_pair(self, target):
        return self.find_pair_with_sum(self.sorted_array, target)

if __name__ == '__main__':
    sample_array = [1, 3, 5, 7, 9, 11]
    target_value = 10
    solver = TwoSumSolver(sample_array)
    result = solver.find_pair(target_value)
    print(result)