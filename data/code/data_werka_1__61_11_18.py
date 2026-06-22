class OutOfBoundsError(ValueError):

    def __init__(self, message):
        super().__init__(message)

def get_element_at_position(lst, index):
    if not isinstance(index, int) or index < 0 or index >= len(lst):
        raise OutOfBoundsError('Index is out of bounds')
    return lst[index]
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    try:
        print(get_element_at_position(sample_list, 2))
        print(get_element_at_position(sample_list, 5))
    except OutOfBoundsError as e:
        print(e)