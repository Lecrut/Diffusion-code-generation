class InvalidPositionError(ValueError):
    def __init__(self, message):
        super().__init__(message)

def is_valid_index(index, length):
    return isinstance(index, int) and 0 <= index < length

def get_element_at_position(lst, index):
    if not is_valid_index(index, len(lst)):
        raise InvalidPositionError('Index is out of bounds')
    return lst[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        print(get_element_at_position(sample_list, 1))
        print(get_element_at_position(sample_list, 6))
    except InvalidPositionError as e:
        print(e)