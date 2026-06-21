def safe_pop(lst, index):
    try:
        element = lst.pop(index)
        return element
    except IndexError:
        raise ValueError("Index out of range")

if __name__ == '__main__':
    SAMPLE_LIST = [5, 15, 25, 35, 45]
    INDEX_TO_POP = 3

    try:
        popped_element = safe_pop(SAMPLE_LIST, INDEX_TO_POP)
        print(f"Popped element: {popped_element}")
        print(f"List after popping: {SAMPLE_LIST}")
    except ValueError as e:
        print(e)