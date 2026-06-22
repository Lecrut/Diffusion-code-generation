class ListIndexer:
    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

if __name__ == '__main__':
    sample_data = [123, 456, 789, 101112, 131415]
    indexer = ListIndexer(sample_data)
    
    try:
        index_to_find = 2
        element = indexer.get_element(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
        
        index_to_find = 0
        element = indexer.get_element(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
        
        index_to_find = 4
        element = indexer.get_element(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
        
    except (ValueError, IndexError) as e:
        print(e)