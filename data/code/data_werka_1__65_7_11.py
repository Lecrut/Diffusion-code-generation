class EnhancedList:
    def __init__(self, elements):
        self._elements = elements

    def get_element(self, index):
        try:
            return self._elements[index]
        except IndexError as e:
            raise IndexError(f"Index {index} is out of bounds") from e

if __name__ == '__main__':
    sample_elements = [5, 15, 25, 35, 45]
    my_enhanced_list = EnhancedList(sample_elements)
    
    index_to_access = 2
    element_at_index = my_enhanced_list.get_element(index_to_access)
    print(f"Element at index {index_to_access}: {element_at_index}")
    
    try:
        invalid_index = 5
        element_at_invalid_index = my_enhanced_list.get_element(invalid_index)
        print(f"Element at index {invalid_index}: {element_at_invalid_index}")
    except IndexError as e:
        print(e)