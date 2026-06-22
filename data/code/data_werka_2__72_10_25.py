import copy

class ElementComparer:

    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise ValueError('Data must be a list')
        if index1 < 0 or index1 >= len(data):
            raise ValueError(f'Index {index1} is out of range for list of length {len(data)}')
        if index2 < 0 or index2 >= len(data):
            raise ValueError(f'Index {index2} is out of range for list of length {len(data)}')
        elem1 = copy.deepcopy(data[index1])
        elem2 = copy.deepcopy(data[index2])
        type1 = type(elem1)
        type2 = type(elem2)
        if type1 != type2:
            return {'equal': False, 'reason': 'Type mismatch', 'type1': type1.__name__, 'type2': type2.__name__, 'value1': elem1, 'value2': elem2}
        if type1 is dict:
            if set(elem1.keys()) != set(elem2.keys()):
                return {'equal': False, 'reason': 'Keys mismatch', 'keys1': list(elem1.keys()), 'keys2': list(elem2.keys()), 'value1': elem1, 'value2': elem2}
            for key in elem1:
                if not self._deep_compare(elem1[key], elem2[key]):
                    return {'equal': False, 'reason': f"Value mismatch at key '{key}'", 'value1': elem1, 'value2': elem2}
            return {'equal': True, 'value1': elem1, 'value2': elem2}
        if type1 is list:
            if len(elem1) != len(elem2):
                return {'equal': False, 'reason': 'Length mismatch', 'len1': len(elem1), 'len2': len(elem2), 'value1': elem1, 'value2': elem2}
            for i in range(len(elem1)):
                if not self._deep_compare(elem1[i], elem2[i]):
                    return {'equal': False, 'reason': f'Element mismatch at index {i}', 'value1': elem1, 'value2': elem2}
            return {'equal': True, 'value1': elem1, 'value2': elem2}
        if elem1 == elem2:
            return {'equal': True, 'value1': elem1, 'value2': elem2}
        return {'equal': False, 'reason': 'Values differ', 'value1': elem1, 'value2': elem2}

    def _deep_compare(self, v1, v2):
        if type(v1) != type(v2):
            return False
        if isinstance(v1, dict):
            if set(v1.keys()) != set(v2.keys()):
                return False
            for k in v1:
                if not self._deep_compare(v1[k], v2[k]):
                    return False
            return True
        if isinstance(v1, list):
            if len(v1) != len(v2):
                return False
            for i in range(len(v1)):
                if not self._deep_compare(v1[i], v2[i]):
                    return False
            return True
        return v1 == v2
if __name__ == '__main__':
    comparer = ElementComparer()
    data1 = [10, 20, 30]
    result1 = comparer.compare_at_spots(data1, 0, 1)
    print(f'Test 1 (integers): {result1}')
    assert result1['equal'] == False
    data2 = [10, 10, 30]
    result2 = comparer.compare_at_spots(data2, 0, 1)
    print(f'Test 2 (equal ints): {result2}')
    assert result2['equal'] == True
    data3 = [10, '10', 30]
    result3 = comparer.compare_at_spots(data3, 0, 1)