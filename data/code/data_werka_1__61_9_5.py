def safe_pop(lst, index):
    try:
        return lst.pop(index)
    except IndexError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    index_to_pop = 3
    popped_element = safe_pop(sample_list, index_to_pop)
    if popped_element is not None:
        print(f"Element removed: {popped_element}")
    print("Remaining list:", sample_list)