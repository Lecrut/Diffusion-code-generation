def all_elements_in_range(lst, min_val, max_val):
    return all(min_val <= x <= max_val for x in lst)

if __name__ == '__main__':
    sample_list = [4, 6, 8, 10]
    lower_bound = 3
    upper_bound = 11
    result = all_elements_in_range(sample_list, lower_bound, upper_bound)
    print(result)