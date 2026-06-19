def safe_pop(lst, index):
    try:
        return lst.pop(index)
    except IndexError:
        print("Index out of range")
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_remove = 2
    removed_element = safe_pop(sample_list, index_to_remove)
    print("Removed element:", removed_element)
    print("Updated list:", sample_list)