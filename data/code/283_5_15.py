def all_elements_in_range(lst, min_val, max_val):
    for element in lst:
        if not (min_val <= element <= max_val):
            return False
    return True

if __name__ == '__main__':
    sample_list = [2, 4, 6, 8]
    lower_bound = 1
    upper_bound = 10
    print(all_elements_in_range(sample_list, lower_bound, upper_bound))