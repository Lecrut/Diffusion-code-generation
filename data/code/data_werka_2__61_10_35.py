class InvalidIndexError(ValueError):
    def __init__(self, message):
        super().__init__(message)

def get_element_at_position(lst, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(lst):
        raise InvalidIndexError(f"Index {index} is out of bounds for list of length {len(lst)}")
    return lst[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        print(get_element_at_position(sample_list, 3))
        print(get_element_at_position(sample_list, 5))
    except (TypeError, InvalidIndexError) as e:
        print(e)