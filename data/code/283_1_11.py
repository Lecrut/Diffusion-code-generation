def all_elements_are_ints(lst):
    return all(isinstance(x, int) for x in lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(all_elements_are_ints(sample_list))
    
    sample_list_with_float = [1, 2, 3.0, 4, 5]
    print(all_elements_are_ints(sample_list_with_float))