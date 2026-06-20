def compare_elements(list1, list2, index):
    return list1[index] <= list2[index]

if __name__ == '__main__':
    data = {
        'list_a': [10, 20, 30],
        'list_b': [15, 25, 35],
        'list_c': [5, 10, 15],
        'list_d': [8, 12, 18],
        'list_e': [100],
        'list_f': [99]
    }
    
    comparisons = {
        (data['list_a'], data['list_b'], 1): compare_elements(data['list_a'], data['list_b'], 1),
        (data['list_c'], data['list_d'], 0): compare_elements(data['list_c'], data['list_d'], 0),
        (data['list_e'], data['list_f'], 0): compare_elements(data['list_e'], data['list_f'], 0)
    }
    
    for key, result in comparisons.items():
        print(f"Comparing {key}: {result}")