class InvalidIndexError(ValueError):

    def __init__(self, message):
        super().__init__(message)

def get_element_at_position(lst, index):
    if not isinstance(index, int) or index < 0 or index >= len(lst):
        raise InvalidIndexError('Index is out of bounds')
    return lst[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_at_position(sample_list, 2))
        print(get_element_at_position(sample_list, 5))
    except InvalidIndexError as e:
        print(e)