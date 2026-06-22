def all_elements_are_integers(lst):
    return all((isinstance(item, int) for item in lst))
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(all_elements_are_integers(sample_list))
    sample_list_with_non_integer = [1, 2, '3', 4, 5]
    print(all_elements_are_integers(sample_list_with_non_integer))