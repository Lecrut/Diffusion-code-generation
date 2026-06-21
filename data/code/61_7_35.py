class ListAccessor:
    def __init__(self, lst):
        self.lst = lst

    def get_element_at_index(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(self.lst):
            raise IndexError("Index out of bounds")
        return self.lst[index]

if __name__ == '__main__':
    SAMPLE_LIST = [123, 456, 789, 101112, 131415]
    INDEX_TO_FIND = 3
    accessor = ListAccessor(SAMPLE_LIST)
    try:
        element = accessor.get_element_at_index(INDEX_TO_FIND)
        print(f"Element at index {INDEX_TO_FIND}: {element}")
    except (ValueError, IndexError) as e:
        print(e)