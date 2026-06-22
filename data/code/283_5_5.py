def all_elements_in_range(lst, min_val, max_val):
    for x in lst:
        if not (min_val <= x <= max_val):
            return False
    return True

if __name__ == '__main__':
    sample_list = [2, 4, 6, 8]
    min_value = 1
    max_value = 10
    result = all_elements_in_range(sample_list, min_value, max_value)
    print(result)