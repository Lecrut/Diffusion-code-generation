def pop_element_from_list(lst, index):
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(index, int):
        raise ValueError("The index must be an integer.")
    try:
        return lst.pop(index)
    except IndexError:
        raise ValueError("Index out of range")

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    INDEX_TO_POP = 2
    try:
        popped_element = pop_element_from_list(SAMPLE_LIST, INDEX_TO_POP)
        print(f"Popped element: {popped_element}")
        print(f"List after popping: {SAMPLE_LIST}")
    except (TypeError, ValueError) as e:
        print(e)