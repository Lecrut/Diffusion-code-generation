def get_first_element(data):
    if not data:
        return None
    return data[0]

if __name__ == '__main__':
    samples = {
        'numbers': [1, 2, 3, 4],
        'letters': ['a', 'b', 'c'],
        'empty': [],
        'single_item': [99]
    }
    
    for name, sample_list in samples.items():
        print(f"First element of {name}: {get_first_element(sample_list)}")