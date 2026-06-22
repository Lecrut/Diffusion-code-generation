class ListElementAccessor:
    def __init__(self, lst):
        self.lst = lst

    def get_element_at_index(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(self.lst):
            raise IndexError("Index out of bounds")
        return self.lst[index]

if __name__ == '__main__':
    sample_list = [1000, 2000, 3000, 4000, 5000]
    accessor = ListElementAccessor(sample_list)
    
    try:
        index_to_find = 2
        element = accessor.get_element_at_index(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
        
        index_to_find = -1
        element = accessor.get_element_at_index(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
    except (ValueError, IndexError) as e:
        print(e)