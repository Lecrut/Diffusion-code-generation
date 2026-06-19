def get_first_element(lst):
    try:
        return lst[0]
    except IndexError as e:
        print(f"Error: The list is empty - {e}")
        return None

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        [],
        ['a', 'b', 'c'],
        [True, False]
    ]
    for i, lst in enumerate(sample_lists):
        first_element = get_first_element(lst)
        print(f"First element of list {i+1}: {first_element}")