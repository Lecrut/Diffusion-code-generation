def find_max(numbers):
    return max(numbers)

if __name__ == '__main__':
    sample_values = {
        'sample_list1': [1, 5, 2, 8, 3],
        'sample_list2': [-10, -5, -20, -1],
        'sample_list3': [42]
    }
    
    for key, value in sample_values.items():
        print(f"Max of {value}: {find_max(value)}")