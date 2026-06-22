import copy

class ElementComparer:
    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise ValueError("Input data must be a list")
        
        if index1 < 0 or index1 >= len(data):
            raise ValueError(f"Index {index1} is out of bounds for list of length {len(data)}")
        
        if index2 < 0 or index2 >= len(data):
            raise ValueError(f"Index {index2} is out of bounds for list of length {len(data)}")
        
        element1 = copy.deepcopy(data[index1])
        element2 = copy.deepcopy(data[index2])
        
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
                "reason": "Values are identical",
                "value1": element1,
                "value2": element2
            }
        
        if isinstance(element1, dict) and isinstance(element2, dict):
            keys1 = set(element1.keys())
            keys2 = set(element2.keys())
            if keys1 != keys2:
                missing_in_2 = keys1 - keys2
                missing_in_1 = keys2 - keys1
                return {
                    "equal": False,
                    "reason": "Dictionary keys differ",
                    "missing_in_element2": list(missing_in_2),
                    "missing_in_element1": list(missing_in_1),
                    "value1": element1,
                    "value2": element2
                }
            
            differences = []
            for key in keys1:
                sub_result = self.compare_at_spots([element1[key], element2[key]], 0, 1)
                if not sub_result["equal"]:
                    differences.append({
                        "key": key,
                        "details": sub_result
                    })
            
            if differences:
                return {
                    "equal": False,
                    "reason": "Nested dictionary differences found",
                    "differences": differences,
                    "value1": element1,
                    "value2": element2
                }
        
        if isinstance(element1, list) and isinstance(element2, list):
            if len(element1) != len(element2):
                return {
                    "equal": False,
                    "reason": "List lengths differ",
                    "len1": len(element1),
                    "len2": len(element2),
                    "value1": element1,
                    "value2": element2
                }
            
            differences = []
            for i in range(len(element1)):
                sub_result = self.compare_at_spots([element1[i], element2[i]], 0, 1)
                if not sub_result["equal"]:
                    differences.append({
                        "index": i,
                        "details": sub_result
                    })
            
            if differences:
                return {
                    "equal": False,
                    "reason": "Nested list differences found",
                    "differences": differences,
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
    
    sample_data = [
        {"name": "Alice", "age": 30, "scores": [90, 85]},
        {"name": "Bob", "age": 30, "scores": [90, 85]},
        [1, 2, 3],
        [1, 2, 4],
        "hello",
        "world"
    ]
    
    result1 = comparer.compare_at_spots(sample_data, 0, 1)
    print(result1)
    
    result2 = comparer.compare_at_spots(sample_data, 2, 3)
    print(result2)
    
    result3 = comparer.compare_at_spots(sample_data, 4, 5)
    print(result3)