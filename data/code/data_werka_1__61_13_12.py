def get_element(sequence, index):
    return sequence[index]

if __name__ == '__main__':
    sample_data = {
        'tuple': (10, 20, 30, 40, 50),
        'list': ['a', 'b', 'c', 'd', 'e']
    }
    
    tuple_element = get_element(sample_data['tuple'], 2)
    list_element = get_element(sample_data['list'], 3)
    
    print(f"Element from tuple at index 2: {tuple_element}")
    print(f"Element from list at index 3: {list_element}")