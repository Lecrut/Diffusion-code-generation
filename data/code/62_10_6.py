def get_second_item(lst):
    return lst[1] if len(lst) > 1 else None

if __name__ == '__main__':
    sample_data = {
        'list_a': [1, 2, 3],
        'list_b': ['apple', 'banana', 'cherry'],
        'list_c': [True, False],
        'list_d': [42]
    }
    
    for label, lst in sample_data.items():
        print(f"The second item in {label} is: {get_second_item(lst)}")