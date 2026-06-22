class ListAccessor:
    def __init__(self, lst):
        self.lst = lst

    def get_element_at_index(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        try:
            return self.lst[index]
        except IndexError:
            raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_list = [50, 60, 70, 80, 90]
    accessor = ListAccessor(sample_list)
    
    try:
        index_to_find = 2
        element = accessor.get_element_at_index(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
        
        index_to_find = 10
        element = accessor.get_element_at_index(index_to_find)
    except (ValueError, IndexError) as e:
        print(e)