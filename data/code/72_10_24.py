import copy

class ElementComparer:
    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise ValueError("Data must be a list")
        if index1 < 0 or index1 >= len(data):
            raise ValueError(f"Index {index1} is out of range for list of length {len(data)}")
        if index2 < 0 or index2 >= len(data):
            raise ValueError(f"Index {index2} is out of range for list of length {len(data)}")
        element1 = copy.deepcopy(data[index1])
        element2 = copy.deepcopy(data[index2])
        if type(element1) != type(element2):
            return {
                "equal": False,
                "reason": "Type mismatch",
                "type1": type(element1).__name__,
                "type2": type(element2).__name__,
                "value1": element1,
                "value2": element2
            }
        if isinstance(element1, dict):
            if element1 == element2:
                return {"equal": True, "reason": "Identical"}
            keys1 = set(element1.keys())
            keys2 = set(element2.keys())
            if keys1 != keys2:
                missing_in_2 = keys1 - keys2
                missing_in_1 = keys2 - keys1
                return {
                    "equal": False,
                    "reason": "Keys mismatch",
                    "missing_in_element2": list(missing_in_2),
                    "missing_in_element1": list(missing_in_1)
                }
            differences = []
            for key in keys1:
                if element1[key] != element2[key]:
                    differences.append(key)
            if differences:
                return {
                    "equal": False,
                    "reason": "Values differ",
                    "different_keys": differences
                }
            return {"equal": True, "reason": "Identical"}
        if isinstance(element1, list):
            if len(element1) != len(element2):
                return {
                    "equal": False,
                    "reason": "Length mismatch",
                    "len1": len(element1),
                    "len2": len(element2)
                }
            for i in range(len(element1)):
                if element1[i] != element2[i]:
                    return {
                        "equal": False,
                        "reason": "Element mismatch at index",
                        "index": i,
                        "value1": element1[i],
                        "value2": element2[i]
                    }
            return {"equal": True, "reason": "Identical"}
        if element1 == element2:
            return {"equal": True, "reason": "Identical"}
        return {
            "equal": False,
            "reason": "Value mismatch",
            "value1": element1,
            "value2": element2
        }

if __name__ == '__main__':
    comparer = ElementComparer()
    data = [1, 2, 3, 4, 5]
    result = comparer.compare_at_spots(data, 0, 1)
    print(result)
    data2 = [{"a": 1}, {"a": 1}]
    result2 = comparer.compare_at_spots(data2, 0, 1)
    print(result2)
    data3 = [1, 2, 3]
    result3 = comparer.compare_at_spots(data3, 0, 2)
    print(result3)