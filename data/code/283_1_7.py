def all_elements_are_ints(lst):
    return all(isinstance(x, int) for x in lst)

if __name__ == '__main__':
    sample_list = [10, 5, 22, 8, 30, 15, 7]
    print(all_elements_are_ints(sample_list))
    
    sample_list_with_non_int = [10, 5, '22', 8, 30, 15.0, 7]
    print(all_elements_are_ints(sample_list_with_non_int))