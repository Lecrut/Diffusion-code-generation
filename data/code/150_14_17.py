def remove_first_occurrence(lst, value):
    try:
        index = lst.index(value)
        del lst[index]
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    value_to_remove1 = 3
    success1 = remove_first_occurrence(sample_list1, value_to_remove1)
    print(f"List: {sample_list1}, Item to remove: {value_to_remove1}, Success: {success1}")

    sample_list2 = [10, 20, 30]
    value_to_remove2 = 99
    success2 = remove_first_occurrence(sample_list2, value_to_remove2)
    print(f"List: {sample_list2}, Item to remove: {value_to_remove2}, Success: {success2}")

    sample_list3 = ['a', 'b', 'c']
    value_to_remove3 = 'd'
    success3 = remove_first_occurrence(sample_list3, value_to_remove3)
    print(f"List: {sample_list3}, Item to remove: {value_to_remove3}, Success: {success3}")