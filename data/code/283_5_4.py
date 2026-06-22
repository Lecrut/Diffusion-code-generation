def all_elements_in_range(lst, lower_bound, upper_bound):
    return all(lower_bound <= x <= upper_bound for x in lst)

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9]
    lower = 2
    upper = 10
    print(all_elements_in_range(sample_list, lower, upper))