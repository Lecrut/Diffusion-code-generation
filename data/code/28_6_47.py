def is_largest_element_larger(lst, target):
    if not lst:
        raise ValueError("The list cannot be empty")
    
    def validate_target():
        if not isinstance(target, (int, float)):
            raise ValueError("Target must be a number")
    
    def find_max_recursive(index):
        if index == len(lst) - 1:
            return lst[index]
        else:
            current_max = find_max_recursive(index + 1)
            return max(lst[index], current_max)
    
    validate_target()
    largest_element = find_max_recursive(0)
    return largest_element > target

if __name__ == '__main__':
    sample_list = [4, 9, 2, 6, 5]
    target_value = 7
    result = is_largest_element_larger(sample_list, target_value)
    print(result)