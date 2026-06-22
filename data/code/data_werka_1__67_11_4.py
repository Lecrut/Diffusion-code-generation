class TwoSumSolver:

    def __init__(self, sorted_array):
        self.sorted_array = sorted_array

    def find_pair_with_sum(self, target):
        left_index = 0
        right_index = len(self.sorted_array) - 1
        while left_index < right_index:
            current_sum = self.sorted_array[left_index] + self.sorted_array[right_index]
            if current_sum == target:
                return (self.sorted_array[left_index], self.sorted_array[right_index])
            elif current_sum < target:
                left_index += 1
            else:
                right_index -= 1
        return None
if __name__ == '__main__':
    sample_array = [1, 3, 5, 7, 9, 11]
    target_value = 10
    solver = TwoSumSolver(sample_array)
    result1 = solver.find_pair_with_sum(target_value)
    print(result1)
    another_target = 16
    result2 = solver.find_pair_with_sum(another_target)
    print(result2)
    non_existent_target = 30
    result3 = solver.find_pair_with_sum(non_existent_target)
    print(result3)