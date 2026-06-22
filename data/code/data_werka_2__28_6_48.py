def is_largest_greater_than_target(lst, target):
    if not lst:
        raise ValueError("List cannot be empty")
    
    def find_max_recursive(index):
        if index == len(lst) - 1:
            return lst[index]
        else:
            current_max = find_max_recursive(index + 1)
            return max(lst[index], current_max)
    
    largest_element = find_max_recursive(0)
    return largest_element > target

if __name__ == '__main__':
    sample_list = [15, 22, 8, 34, 19]
    target_value = 20
    result = is_largest_greater_than_target(sample_list, target_value)
    print(result)