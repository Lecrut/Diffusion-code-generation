def is_within_range(element, min_val, max_val):
    return min_val <= element <= max_val

def all_elements_in_range(lst, min_val, max_val):
    if not lst:
        return False
    for element in lst:
        if not isinstance(element, (int, float)) or not is_within_range(element, min_val, max_val):
            return False
    return True

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9]
    min_value = 2
    max_value = 10
    print(all_elements_in_range(sample_list, min_value, max_value))