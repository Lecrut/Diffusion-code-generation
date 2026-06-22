def are_all_integers(lst):
    return all((isinstance(x, int) for x in lst))
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    print(are_all_integers(sample_list1))
    sample_list2 = [1, 2, '3', 4]
    print(are_all_integers(sample_list2))