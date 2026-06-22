class IndexAccessor:
    def __init__(self, elements):
        self.elements = elements

    def retrieve_element(self, index):
        try:
            return self.elements[index]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    indices_to_test = [1, 4, -1, 5, 2]
    accessor = IndexAccessor(sample_data)
    
    for index in indices_to_test:
        result = accessor.retrieve_element(index)
        print(f"Element at index {index}: {result}")