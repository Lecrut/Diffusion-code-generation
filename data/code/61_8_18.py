class ListElementAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_element(self, index):
        if 0 <= index < len(self.data_list):
            return self.data_list[index]
        else:
            raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    accessor = ListElementAccessor(sample_data)
    
    try:
        index_to_find = 2
        result1 = accessor.get_element(index_to_find)
        print(f"Element at index {index_to_find}: {result1}")
        
        index_to_find = 4
        result2 = accessor.get_element(index_to_find)
        print(f"Element at index {index_to_find}: {result2}")
    except IndexError as e:
        print(f"Error: {e}")