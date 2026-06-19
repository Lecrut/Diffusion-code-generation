def validate_list(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if not data:
        raise IndexError("list is empty")

def get_first_element(data):
    validate_list(data)
    return data[0]

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30],
        ['x', 'y', 'z'],
        []
    ]
    
    for lst in sample_lists:
        try:
            print(f"First element of {lst}: {get_first_element(lst)}")
        except (IndexError, TypeError) as e:
            print(f"Error processing {lst}: {e}")