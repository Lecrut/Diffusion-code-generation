class TwoSumSolver:
    def __init__(self, sorted_array):
        self.sorted_array = sorted_array

    def find_pair(self, target_sum):
        left_index = 0
        right_index = len(self.sorted_array) - 1

        while left_index < right_index:
            current_sum = self.sorted_array[left_index] + self.sorted_array[right_index]
            if current_sum == target_sum:
                return (self.sorted_array[left_index], self.sorted_array[right_index])
            elif current_sum < target_sum:
                left_index += 1
            else:
                right_index -= 1

        return None

if __name__ == '__main__':
    sample_array = [1, 3, 5, 7, 9, 11]
    target_value_1 = 10
    target_value_2 = 16

    solver = TwoSumSolver(sample_array)
    
    result_1 = solver.find_pair(target_value_1)
    print(f"Pair for sum {target_value_1}: {result_1}")

    result_2 = solver.find_pair(target_value_2)
    print(f"Pair for sum {target_value_2}: {result_2}")