def pop_element_from_list(lst, index):
    if not isinstance(lst, list):
        raise ValueError("Provided argument is not a list")
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    try:
        element = lst.pop(index)
        return element
    except IndexError:
        print("Index out of range")
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [5, 15, 25, 35, 45]
    INDEX_TO_POP = 3
    popped_element = pop_element_from_list(SAMPLE_LIST, INDEX_TO_POP)
    print("Popped element:", popped_element)
    print("List after popping:", SAMPLE_LIST)