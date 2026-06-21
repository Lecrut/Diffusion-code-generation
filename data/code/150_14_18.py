def remove_first_occurrence(lst, value):
    try:
        index = lst.index(value)
        del lst[index]
    except ValueError:
        return

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 2, 6]
    value_to_remove1 = 2
    remove_first_occurrence(sample_list1, value_to_remove1)
    print(f"List after removing {value_to_remove1}: {sample_list1}")

    sample_list2 = [10, 20, 30]
    value_to_remove2 = 99
    remove_first_occurrence(sample_list2, value_to_remove2)
    print(f"List after attempting to remove {value_to_remove2}: {sample_list2}")

    sample_list3 = ['a', 'b', 'c']
    value_to_remove3 = 'd'
    remove_first_occurrence(sample_list3, value_to_remove3)
    print(f"List after attempting to remove {value_to_remove3}: {sample_list3}")