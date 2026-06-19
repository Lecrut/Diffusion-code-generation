def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_data = {
        'list': [10, 20, 30, 40, 50],
        'tuple': (5, 15, 25, 35),
        'string': "HelloWorld"
    }
    
    index_to_find = 2
    for key, value in sample_data.items():
        element = get_element(value, index_to_find)
        print(f"Element at index {index_to_find} in the {key}: {element}")