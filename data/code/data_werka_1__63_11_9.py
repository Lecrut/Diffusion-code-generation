def get_first_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

def validate_list(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) == 0:
        raise ValueError("List cannot be empty")

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4],
        ['a', 'b', 'c'],
        []
    ]

    for lst in sample_lists:
        try:
            validate_list(lst)
            print(f"First element of {lst}: {get_first_element(lst)}")
        except Exception as e:
            print(f"Error caught: {e}")