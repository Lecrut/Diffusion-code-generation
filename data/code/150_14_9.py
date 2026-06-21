def remove_first_occurrence(lst, value):
    try:
        lst.remove(value)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    value_to_remove = 3
    success = remove_first_occurrence(sample_list, value_to_remove)
    print(f"List: {sample_list}, Value to Remove: {value_to_remove}, Success: {success}")