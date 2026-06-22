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
        
        if type(element1) != type(element2):
            return False
        
        if isinstance(element1, dict):
            if set(element1.keys()) != set(element2.keys()):
                return False
            for key in element1:
                if not self._deep_compare(element1[key], element2[key]):
                    return False
            return True
        
        if isinstance(element1, list):
            if len(element1) != len(element2):
                return False
            for i in range(len(element1)):
                if not self._deep_compare(element1[i], element2[i]):
                    return False
            return True
        
        if isinstance(element1, tuple):
            if len(element1) != len(element2):
                return False
            for i in range(len(element1)):
                if not self._deep_compare(element1[i], element2[i]):
                    return False
            return True
        
        if isinstance(element1, set):
            if element1 != element2:
                return False
            return True
        
        if isinstance(element1, (int, float, str, bool, type(None))):
            return element1 == element2
        
        if hasattr(element1, '__dict__') and hasattr(element2, '__dict__'):
            if type(element1) != type(element2):
                return False
            return element1.__dict__ == element2.__dict__
        
        return element1 == element2

    def _deep_compare(self, obj1, obj2):
        if type(obj1) != type(obj2):
            return False
        
        if isinstance(obj1, dict):
            if set(obj1.keys()) != set(obj2.keys()):
                return False
            for key in obj1:
                if not self._deep_compare(obj1[key], obj2[key]):
                    return False
            return True
        
        if isinstance(obj1, list):
            if len(obj1) != len(obj2):
                return False
            for i in range(len(obj1)):
                if not self._deep_compare(obj1[i], obj2[i]):
                    return False
            return True
        
        if isinstance(obj1, tuple):
            if len(obj1) != len(obj2):
                return False
            for i in range(len(obj1)):
                if not self._deep_compare(obj1[i], obj2[i]):
                    return False
            return True
        
        if isinstance(obj1, set):
            return obj1 == obj2
        
        if isinstance(obj1, (int, float, str, bool, type(None))):
            return obj1 == obj2
        
        if hasattr(obj1, '__dict__') and hasattr(obj2, '__dict__'):
            if type(obj1) != type(obj2):
                return False
            return obj1.__dict__ == obj2.__dict__
        
        return obj1 == obj2

if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [1, 2, [1, 2], {'a': 1}, {'a': 2}, [1, 2], 1]
    
    result1 = comparer.compare_at_spots(sample_data, 0, 6)
    print(result1)
    
    result2 = comparer.compare_at_spots(sample_data, 2, 5)
    print(result2)
    
    result3 = comparer.compare_at_spots(sample_data, 3, 4)
    print(result3)
    
    result4 = comparer.compare_at_spots(sample_data, 0, 1)
    print(result4)