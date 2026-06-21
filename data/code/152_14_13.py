def intersect_lists(list_a, list_b):
    set_b = set(list_b)
    return [item for item in list_a if item in set_b]
if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [40, 50, 60, 70, 80]
    shared_items = intersect_lists(sample_list1, sample_list2)
    print(shared_items)