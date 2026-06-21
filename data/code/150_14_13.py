def remove_first_occurrence(lst, value):
    if value in lst:
        lst.remove(value)

if __name__ == '__main__':
    sample_list = [5, 3, 2, 4, 3, 1]
    value_to_remove = 3
    remove_first_occurrence(sample_list, value_to_remove)
    print(sample_list)