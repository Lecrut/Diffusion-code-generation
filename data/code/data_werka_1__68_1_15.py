def find_element_differences(list1, list2):
    def compute_difference(pair):
        return abs(pair[0] - pair[1])
    
    differences = [compute_difference((a, b)) for a, b in zip(list1, list2)]
    return differences

if __name__ == '__main__':
    data = {
        'list_a': [1, 5, 10, 15],
        'list_b': [3, 7, 8, 12]
    }
    result = find_element_differences(data['list_a'], data['list_b'])
    print(result)