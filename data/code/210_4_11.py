def find_range(data):
    return (min(data), max(data))

if __name__ == '__main__':
    sample_values = {
        'list1': [1, 5, 2, 8, 3],
        'list2': [],
        'list3': [10],
        'list4': [-5, 0, 5]
    }
    
    for key, value in sample_values.items():
        print(f"Range of {key}: {find_range(value)}")