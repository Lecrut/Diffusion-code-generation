def is_largest_element_larger(lst, target):
    if not lst:
        raise ValueError("The list cannot be empty")
    
    def recursive_max(index):
        if index == 0:
            return lst[0]
        else:
            current_max = recursive_max(index - 1)
            return max(current_max, lst[index])
    
    largest_element = recursive_max(len(lst) - 1)
    return largest_element > target

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_value = 25
    result = is_largest_element_larger(sample_list, target_value)
    print(result)