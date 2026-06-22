import copy

class ElementComparer:
    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise ValueError("Input data must be a list")
        
        if index1 < 0 or index1 >= len(data):
            raise ValueError(f"Index {index1} is out of range for list of length {len(data)}")
        
        if index2 < 0 or index2 >= len(data):
            raise ValueError(f"Index {index2} is out of range for list of length {len(data)}")
        
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
                val1 = element1[key]
                val2 = element2[key]
                if val1 != val2:
                    differences.append({
                        "key": key,
                        "value1": val1,
                        "value2": val2
                    })
            
            if differences:
                return {
                    "equal": False,
                    "reason": "Dictionary values differ",
                    "differences": differences,
                    "value1": element1,
                    "value2": element2
                }
        
        if isinstance(element1, list) and isinstance(element2, list):
            if len(element1) != len(element2):
                return {
                    "equal": False,
                    "reason": "List lengths differ",
                    "length1": len(element1),
                    "length2": len(element2),
                    "value1": element1,
                    "value2": element2
                }
            
            differences = []
            for i in range(len(element1)):
                if element1[i] != element2[i]:
                    differences.append({
                        "index": i,
                        "value1": element1[i],
                        "value2": element2[i]
                    })
            
            if differences:
                return {
                    "equal": False,
                    "reason": "List values differ",
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
        [1, 2, 3],
        {"a": 1, "b": 2},
        [1, 2, 3],
        {"a": 1, "b": 3},
        42,
        42
    ]
    
    result1 = comparer.compare_at_spots(sample_data, 0, 2)
    print(result1)
    
    result2 = comparer.compare_at_spots(sample_data, 1, 3)
    print(result2)
    
    result3 = comparer.compare_at_spots(sample_data, 4, 5)
    print(result3)