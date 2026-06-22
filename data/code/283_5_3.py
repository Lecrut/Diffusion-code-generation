def all_elements_in_range(lst, min_val, max_val):
    return all(min_val <= x <= max_val for x in lst)

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9]
    min_value = 2
    max_value = 10
    print(all_elements_in_range(sample_list, min_value, max_value))