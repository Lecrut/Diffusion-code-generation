def get_first_element(data):
    if not data:
        raise IndexError("The provided list is empty")
    return data[0]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        ['x', 'y', 'z'],
        [],
        [True, False],
        [None, None]
    ]
    
    for i, lst in enumerate(sample_lists):
        try:
            print(f"First element of list {i+1}: {get_first_element(lst)}")
        except IndexError as e:
            print(f"Error processing list {i+1}: {e}")