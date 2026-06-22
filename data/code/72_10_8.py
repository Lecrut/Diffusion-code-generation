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
        if element1 == element2:
            return {
                "equal": True,
                "reason": "Values are identical",
                "value": element1
            }
        return {
            "equal": False,
            "reason": "Values differ",
            "value1": element1,
            "value2": element2
        }

if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [1, 2, [3, 4], [3, 4], "hello"]
    result = comparer.compare_at_spots(sample_data, 2, 3)
    print(result)
    result2 = comparer.compare_at_spots(sample_data, 0, 1)
    print(result2)
    result3 = comparer.compare_at_spots(sample_data, 2, 4)
    print(result3)