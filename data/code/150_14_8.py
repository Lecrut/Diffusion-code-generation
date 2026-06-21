def remove_first_occurrence(lst, value):
    try:
        index = lst.index(value)
        del lst[index]
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 6]
    print("Original list:", sample_list)
    success = remove_first_occurrence(sample_list, 2)
    print("Modified list:", sample_list)
    print("Success:", success)