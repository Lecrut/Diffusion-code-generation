class OutOfBoundsError(ValueError):

    def __init__(self, message):
        super().__init__(message)

def is_valid_index(index, length):
    return isinstance(index, int) and 0 <= index < length

def get_element_at_position(lst, index):
    if not is_valid_index(index, len(lst)):
        raise OutOfBoundsError('Index is out of bounds')
    return lst[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_at_position(sample_list, 2))
        print(get_element_at_position(sample_list, 5))
    except OutOfBoundsError as e:
        print(e)