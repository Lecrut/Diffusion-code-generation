def is_largest_element_larger(lst, target):
    if not lst:
        raise ValueError("The list cannot be empty")
    
    def validate_list_elements():
        for element in lst:
            if not isinstance(element, (int, float)):
                raise ValueError("All elements in the list must be numbers")

    def find_max_recursive(index):
        if index == 0:
            return lst[0]
        else:
            current_max = find_max_recursive(index - 1)
            return max(current_max, lst[index])
    
    validate_list_elements()
    largest_element = find_max_recursive(len(lst) - 1)
    return largest_element > target

if __name__ == '__main__':
    sample_list = [4.5, 3.2, 7.8, 6.0, 9.1]
    target_value = 8.0
    result = is_largest_element_larger(sample_list, target_value)
    print(result)