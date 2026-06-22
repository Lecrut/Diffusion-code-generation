class ListAccessor:
    def __init__(self, elements):
        self.elements = elements

    def get_element_by_index(self, index):
        try:
            return self.elements[index]
        except IndexError:
            return None

    def get_elements_by_indices(self, indices):
        return [self.get_element_by_index(i) for i in indices]

def access_elements(lst, *indices):
    accessor = ListAccessor(lst)
    return accessor.get_elements_by_indices(indices)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Sample List:", sample_list)
    
    indices_to_access = (0, 2, -1, 4, -2)
    accessed_elements = access_elements(sample_list, *indices_to_access)
    
    for idx, value in zip(indices_to_access, accessed_elements):
        print(f"Element at index {idx}: {value}")