def remove_first_occurrence(lst, value):
    try:
        index = lst.index(value)
        del lst[index]
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2]
    value_to_remove = 2
    success = remove_first_occurrence(sample_list, value_to_remove)
    print(f"List after removal: {sample_list}, Success: {success}")