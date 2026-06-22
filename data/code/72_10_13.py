import copy

class ElementComparer:
    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise ValueError("Data must be a list")
        
        if index1 < 0 or index1 >= len(data):
            raise ValueError(f"Index {index1} is out of bounds for list of length {len(data)}")
        
        if index2 < 0 or index2 >= len(data):
            raise ValueError(f"Index {index2} is out of bounds for list of length {len(data)}")
        
        element1 = copy.deepcopy(data[index1])
        element2 = copy.deepcopy(data[index2])
        
        if element1 == element2:
            return True
        
        return False

if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [1, 2, [1, 2], [1, 2], "hello", "world"]
    result1 = comparer.compare_at_spots(sample_data, 0, 1)
    result2 = comparer.compare_at_spots(sample_data, 2, 3)
    result3 = comparer.compare_at_spots(sample_data, 4, 5)
    print(result1)
    print(result2)
    print(result3)