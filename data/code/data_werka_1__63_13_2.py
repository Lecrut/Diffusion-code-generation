def retrieve_first_element(sequence):
    try:
        return sequence[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_data = {
        'list': [1, 2, 3],
        'tuple': (4, 5, 6),
        'empty_list': [],
        'empty_tuple': ()
    }
    
    for key, value in sample_data.items():
        print(f"First element of {key}: {retrieve_first_element(value)}")