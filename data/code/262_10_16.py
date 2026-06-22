def find_min_max(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    def initialize_extremes(nums):
        return nums[0], nums[0]
    
    def update_extremes(current_min, current_max, num):
        if num < current_min:
            current_min = num
        elif num > current_max:
            current_max = num
        return current_min, current_max
    
    min_num, max_num = initialize_extremes(numbers)
    for num in numbers[1:]:
        min_num, max_num = update_extremes(min_num, max_num, num)
    
    return min_num, max_num

if __name__ == '__main__':
    sample_values = [34, 78, 12, 56, 90, 23]
    print(find_min_max(sample_values))