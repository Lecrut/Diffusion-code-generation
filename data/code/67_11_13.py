class TwoPointerFinder:
    def __init__(self, sorted_array):
        self.array = sorted_array

    def find_pair_with_sum(self, target):
        left_index = 0
        right_index = len(self.array) - 1
        
        while left_index < right_index:
            current_sum = self.array[left_index] + self.array[right_index]
            if current_sum == target:
                return (self.array[left_index], self.array[right_index])
            elif current_sum < target:
                left_index += 1
            else:
                right_index -= 1
        
        return None

if __name__ == '__main__':
    sample_sorted_array = [2, 3, 5, 7, 8, 10]
    finder = TwoPointerFinder(sample_sorted_array)
    
    target_value_1 = 13
    result_1 = finder.find_pair_with_sum(target_value_1)
    print(f"Pair with sum {target_value_1}: {result_1}")
    
    target_value_2 = 18
    result_2 = finder.find_pair_with_sum(target_value_2)
    print(f"Pair with sum {target_value_2}: {result_2}")