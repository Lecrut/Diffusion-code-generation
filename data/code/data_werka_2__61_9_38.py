class SafeListAccessor:
    def __init__(self, data):
        self.data = data
    
    def retrieve_element(self, index):
        if index < 0 or index >= len(self.data):
            raise ValueError("Index out of bounds")
        return self.data[index]

if __name__ == '__main__':
    sample_data = [7, 17, 27, 37, 47]
    target_index = 1
    accessor = SafeListAccessor(sample_data)
    
    try:
        element = accessor.retrieve_element(target_index)
        print(f"Element at index {target_index}: {element}")
    except ValueError as e:
        print(e)