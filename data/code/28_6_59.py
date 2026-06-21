def is_largest_element_larger(lst, target):
    if not lst:
        raise ValueError("The list cannot be empty")
    
    def find_max_recursive(index):
        if index == 0:
            return lst[0]
        current_max = find_max_recursive(index - 1)
        return max(current_max, lst[index])
    
    largest_element = find_max_recursive(len(lst) - 1)
    return largest_element > target

if __name__ == '__main__':
    sample_list = [1, 4, 9, 2, 6]
    target_value = 7
    result = is_largest_element_larger(sample_list, target_value)
    print(result)