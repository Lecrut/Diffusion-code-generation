def is_largest_element_greater(lst, target):
    if not lst:
        raise ValueError("The list cannot be empty")
    
    def max_recursive(index):
        if index == len(lst) - 1:
            return lst[index]
        else:
            current_max = max_recursive(index + 1)
            return max(lst[index], current_max)
    
    largest_element = max_recursive(0)
    return largest_element > target

if __name__ == '__main__':
    sample_list = [1, 9, 4, 6, 3]
    target_value = 7
    result = is_largest_element_greater(sample_list, target_value)
    print(result)