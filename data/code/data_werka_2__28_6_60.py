def is_largest_element_greater_than_target(lst, target):
    if not lst:
        raise ValueError("The list cannot be empty")
    
    def find_max_recursive(index):
        if index == len(lst) - 1:
            return lst[index]
        else:
            current_max = find_max_recursive(index + 1)
            return max(lst[index], current_max)
    
    largest_element = find_max_recursive(0)
    return largest_element > target

if __name__ == '__main__':
    sample_list = [3, 5, 7, 2, 8]
    target_value = 6
    result = is_largest_element_greater_than_target(sample_list, target_value)
    print(result)