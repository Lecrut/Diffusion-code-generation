def all_elements_are_ints(lst):
    return all(isinstance(x, int) for x in lst)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = all_elements_are_ints(sample_list)
    print(result)

    sample_list_with_non_int = [10, 20, '30', 40]
    result = all_elements_are_ints(sample_list_with_non_int)
    print(result)