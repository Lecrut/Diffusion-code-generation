def safe_pop(lst, index):
    try:
        return lst.pop(index)
    except IndexError:
        print("Error: Index out of bounds.")
        return None

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    index_to_remove = 3
    if 0 <= index_to_remove < len(sample_list):
        removed_element = safe_pop(sample_list, index_to_remove)
        print(f"Element removed: {removed_element}")
        print(f"List after removal: {sample_list}")
    else:
        print("Error: Invalid index.")