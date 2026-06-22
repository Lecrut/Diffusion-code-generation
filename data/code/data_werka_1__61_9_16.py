def safe_pop(lst, index):
    if not (0 <= index < len(lst)):
        print("Error: Index out of bounds.")
        return None
    return lst.pop(index)

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    index_to_pop = 2
    removed_element = safe_pop(my_list, index_to_pop)
    if removed_element is not None:
        print(f"Element removed: {removed_element}")
        print(f"List after pop: {my_list}")