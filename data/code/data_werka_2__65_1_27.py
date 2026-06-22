class ListAccessor:
    def __init__(self, elements):
        self.elements = elements

    def get_element(self, position):
        if not isinstance(position, int):
            raise TypeError("Position must be an integer")
        if position < 0 or position >= len(self.elements):
            raise IndexError("Position out of range")
        return self.elements[position]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    accessor = ListAccessor(sample_list)
    
    try:
        element_at_index_3 = accessor.get_element(3)
        print(f"Element at index 3: {element_at_index_3}")
        
        element_at_index_0 = accessor.get_element(0)
        print(f"Element at index 0: {element_at_index_0}")
        
    except (IndexError, TypeError) as e:
        print(e)