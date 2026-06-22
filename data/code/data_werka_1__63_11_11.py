def get_first_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    sample_lists = [[1, 2, 3], ['x', 'y', 'z'], [True, False, True]]
    for lst in sample_lists:
        try:
            print(f"First element of {lst}: {get_first_element(lst)}")
        except ValueError as e:
            print(f"Caught error: {e}")