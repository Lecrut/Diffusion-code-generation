def is_largest_element_greater_than_target(lst, target):
    if not lst:
        raise ValueError("The list cannot be empty")
    
    def find_max_recursive(index):
        if index == 0:
            return lst[index]
        else:
            current_max = find_max_recursive(index - 1)
            return max(current_max, lst[index])
    
    largest_element = find_max_recursive(len(lst) - 1)
    return largest_element > target

if __name__ == '__main__':
    SAMPLE_LIST = [42, 35, 67, 89, 12]
    TARGET_VALUE = 50
    result = is_largest_element_greater_than_target(SAMPLE_LIST, TARGET_VALUE)
    print(result)