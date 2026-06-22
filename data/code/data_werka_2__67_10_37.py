class TwoSumSolver:
    def __init__(self, sorted_array):
        self.array = sorted_array

    def find_pair(self, target_sum):
        left_index = 0
        right_index = len(self.array) - 1
        while left_index < right_index:
            current_sum = self.array[left_index] + self.array[right_index]
            if current_sum == target_sum:
                return (self.array[left_index], self.array[right_index])
            elif current_sum < target_sum:
                left_index += 1
            else:
                right_index -= 1
        raise ValueError("No two elements sum up to the target value")

if __name__ == '__main__':
    sample_array = [0, 2, 5, 7, 9, 11]
    target_value = 14
    solver = TwoSumSolver(sample_array)
    result1 = solver.find_pair(target_value)
    print("First pair found:", result1)

    another_target = 16
    try:
        result2 = solver.find_pair(another_target)
        print("Second pair found:", result2)
    except ValueError as e:
        print(e)