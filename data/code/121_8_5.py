def compare_element_counts(structure1, structure2):
    def count_elements(structure):
        if isinstance(structure, list):
            count = 0
            for item in structure:
                count += count_elements(item)
            return count
        elif isinstance(structure, (dict, tuple, set)):
            count = 0
            if isinstance(structure, dict):
                for value in structure.values():
                    count += count_elements(value)
            elif isinstance(structure, tuple) or isinstance(structure, set):
                for item in structure:
                    count += count_elements(item)
            return count
        else:
            return 1
    count1 = count_elements(structure1)
    count2 = count_elements(structure2)
    return count1, count2
if __name__ == '__main__':
    data1 = [1, [2, 3], {'a': 4, 'b': [5]}]
    data2 = [1, [2, 3], {'a': 4, 'b': [5]}]
    data3 = [1, [2, 3], {'a': 4, 'c': [5]}]
    data4 = [1, [2, 3], {'a': 4, 'b': [5, 6]}]
    c1, c2 = compare_element_counts(data1, data2)
    print(f"Data 1 element count: {c1}")
    print(f"Data 2 element count: {c2}")
    print(f"Are counts equal (Data 1 vs Data 2)? {c1 == c2}\n")
    c3, c4 = compare_element_counts(data3, data4)
    print(f"Data 3 element count: {c3}")
    print(f"Data 4 element count: {c4}")
    print(f"Are counts equal (Data 3 vs Data 4)? {c3 == c4}")