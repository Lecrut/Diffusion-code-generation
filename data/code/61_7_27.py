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
    sample_list = [10000, 20000, 30000, 40000, 50000]
    accessor = ListAccessor(sample_list)
    
    try:
        index_to_find = 3
        element = accessor.get_element_at_index(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
    except (ValueError, IndexError) as e:
        print(e)

    try:
        index_to_find = 5
        element = accessor.get_element_at_index(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
    except (ValueError, IndexError) as e:
        print(e)