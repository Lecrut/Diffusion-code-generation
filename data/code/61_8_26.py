MAX_INDEX = 4

def safe_pop(lst, index):
    if index < 0 or index > MAX_INDEX:
        raise ValueError("Index out of range")
    return lst.pop(index)

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    INDEX_TO_POP = 2
    try:
        popped_element = safe_pop(SAMPLE_LIST, INDEX_TO_POP)
        print("Popped element:", popped_element)
        print("List after popping:", SAMPLE_LIST)
    except ValueError as e:
        print(e)