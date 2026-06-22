class FastList:
    def __init__(self, elements):
        self.elements = list(elements)

    def get_element(self, index):
        return self.elements[index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    fast_list = FastList(sample_data)
    
    index_to_access = 2
    element_at_index = fast_list.get_element(index_to_access)
    print(f"Element at index {index_to_access}: {element_at_index}")

    another_index = 4
    another_element = fast_list.get_element(another_index)
    print(f"Element at index {another_index}: {another_element}")