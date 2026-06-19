def get_element(sequence, index):
    if 0 <= index < len(sequence):
        return sequence[index]
    else:
        return None

if __name__ == '__main__':
    sample_data = {
        'list': [10, 20, 30, 40, 50],
        'tuple': (5, 15, 25, 35)
    }
    
    index_to_find = 2
    list_element = get_element(sample_data['list'], index_to_find)
    tuple_element = get_element(sample_data['tuple'], index_to_find)
    
    print(f"Element at index {index_to_find} in the list: {list_element}")
    print(f"Element at index {index_to_find} in the tuple: {tuple_element}")