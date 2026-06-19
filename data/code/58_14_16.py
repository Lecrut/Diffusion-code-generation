def get_first_element(lst):
    try:
        return lst[0]
    except (TypeError, IndexError) as e:
        print(f"Error accessing first element: {e}")
        return None

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        [],
        ['apple', 'banana', 'cherry'],
        None,
        "not a list"
    ]
    for i, lst in enumerate(sample_lists):
        print(f"First element of input {i+1}: {get_first_element(lst)}")