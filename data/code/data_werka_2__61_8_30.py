def validate_index(lst, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range")

def pop_element_from_list(lst, index):
    validate_index(lst, index)
    return lst.pop(index)

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    INDEX_TO_POP = 2
    try:
        popped_element = pop_element_from_list(SAMPLE_LIST, INDEX_TO_POP)
        print("Popped element:", popped_element)
        print("List after popping:", SAMPLE_LIST)
    except (TypeError, IndexError) as e:
        print(e)