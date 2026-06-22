def get_first_element(data):
    if not data:
        raise IndexError("list is empty")
    return data[0]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        ['x', 'y', 'z'],
        [],
        [42],
        ['a']
    ]
    
    for i, lst in enumerate(sample_lists):
        try:
            first_element = get_first_element(lst)
            print(f"First element of list {i+1}: {first_element}")
        except IndexError as e:
            print(f"Error processing list {i+1}: {e}")