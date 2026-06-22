class ElementComparer:
    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise ValueError("Data must be a list")
        
        if index1 < 0 or index1 >= len(data):
            raise ValueError(f"Index {index1} is out of range")
        
        if index2 < 0 or index2 >= len(data):
            raise ValueError(f"Index {index2} is out of range")
        
        element1 = data[index1]
        element2 = data[index2]
        
        if type(element1) != type(element2):
            return {
                "equal": False,
                "reason": "Types differ",
                "type1": type(element1).__name__,
                "type2": type(element2).__name__,
                "value1": element1,
                "value2": element2
            }
        
        if element1 == element2:
            return {
                "equal": True,
                "reason": "Values are equal",
                "value1": element1,
                "value2": element2
            }
        
        if isinstance(element1, (list, tuple)):
            if len(element1) != len(element2):
                return {
                    "equal": False,
                    "reason": "Lengths differ",
                    "length1": len(element1),
                    "length2": len(element2),
                    "value1": element1,
                    "value2": element2
                }
            
            for i in range(len(element1)):
                sub_result = self.compare_at_spots([element1[i], element2[i]], 0, 1)
                if not sub_result["equal"]:
                    return {
                        "equal": False,
                        "reason": f"Element at index {i} differs",
                        "sub_result": sub_result,
                        "value1": element1,
                        "value2": element2
                    }
            
            return {
                "equal": True,
                "reason": "Nested structures are equal",
                "value1": element1,
                "value2": element2
            }
        
        if isinstance(element1, dict):
            if set(element1.keys()) != set(element2.keys()):
                return {
                    "equal": False,
                    "reason": "Keys differ",
                    "keys1": list(element1.keys()),
                    "keys2": list(element2.keys()),
                    "value1": element1,
                    "value2": element2
                }
            
            for key in element1:
                sub_result = self.compare_at_spots([element1[key], element2[key]], 0, 1)
                if not sub_result["equal"]:
                    return {
                        "equal": False,
                        "reason": f"Value for key '{key}' differs",
                        "sub_result": sub_result,
                        "value1": element1,
                        "value2": element2
                    }
            
            return {
                "equal": True,
                "reason": "Dictionaries are equal",
                "value1": element1,
                "value2": element2
            }
        
        return {
            "equal": False,
            "reason": "Values differ",
            "value1": element1,
            "value2": element2
        }

if __name__ == '__main__':
    comparer = ElementComparer()
    
    sample_data = [1, 2, [3, 4], {"a": 5}, "hello"]
    
    result1 = comparer.compare_at_spots(sample_data, 0, 1)
    print(result1)
    
    result2 = comparer.compare_at_spots(sample_data, 2, 2)
    print(result2)
    
    sample_data2 = [[1, 2], [1, 2]]
    result3 = comparer.compare_at_spots(sample_data2, 0, 1)
    print(result3)
    
    sample_data3 = [{"x": 1}, {"x": 1}]
    result4 = comparer.compare_at_spots(sample_data3, 0, 1)
    print(result4)