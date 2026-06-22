import copy

class ElementComparer:

    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise ValueError('Data must be a list')
        if index1 < 0 or index1 >= len(data):
            raise ValueError(f'Index {index1} is out of range for list of length {len(data)}')
        if index2 < 0 or index2 >= len(data):
            raise ValueError(f'Index {index2} is out of range for list of length {len(data)}')
        element1 = copy.deepcopy(data[index1])
        element2 = copy.deepcopy(data[index2])
        if type(element1) != type(element2):
            return {'equal': False, 'reason': 'Type mismatch', 'type1': type(element1).__name__, 'type2': type(element2).__name__, 'value1': element1, 'value2': element2}
        if isinstance(element1, dict):
            if set(element1.keys()) != set(element2.keys()):
                return {'equal': False, 'reason': 'Dictionary keys mismatch', 'keys1': sorted(element1.keys()), 'keys2': sorted(element2.keys())}
            for key in element1:
                sub_result = self.compare_at_spots([element1[key], element2[key]], 0, 1)
                if not sub_result['equal']:
                    return {'equal': False, 'reason': f"Value mismatch at key '{key}'", 'value1': element1[key], 'value2': element2[key]}
            return {'equal': True, 'reason': 'Identical'}
        if isinstance(element1, list):
            if len(element1) != len(element2):
                return {'equal': False, 'reason': 'List length mismatch', 'len1': len(element1), 'len2': len(element2)}
            for i in range(len(element1)):
                sub_result = self.compare_at_spots([element1[i], element2[i]], 0, 1)
                if not sub_result['equal']:
                    return {'equal': False, 'reason': f'Value mismatch at index {i}', 'value1': element1[i], 'value2': element2[i]}
            return {'equal': True, 'reason': 'Identical'}
        if element1 == element2:
            return {'equal': True, 'reason': 'Identical'}
        else:
            return {'equal': False, 'reason': 'Value mismatch', 'value1': element1, 'value2': element2}
if __name__ == '__main__':
    comparer = ElementComparer()
    data1 = [10, 20, 30]
    result1 = comparer.compare_at_spots(data1, 0, 1)
    print('Test 1 (Integers):', result1)
    data2 = ['hello', 'world']
    result2 = comparer.compare_at_spots(data2, 0, 1)
    print('Test 2 (Strings):', result2)
    data3 = [[1, 2], [1, 2]]
    result3 = comparer.compare_at_spots(data3, 0, 1)
    print('Test 3 (Nested Lists):', result3)
    try:
        comparer.compare_at_spots(data1, 0, 5)
    except ValueError as e:
        print('Test 4 (Error):', e)
    data4 = [{'a': 1}, {'a': 1}]
    result5 = comparer.compare_at_spots(data4, 0, 1)
    print('Test 5 (Dicts):', result5)