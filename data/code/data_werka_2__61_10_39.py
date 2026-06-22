class CustomValueError(ValueError):

    def __init__(self, message):
        super().__init__(message)

def validate_index(index, length):
    if not isinstance(index, int):
        raise TypeError('Index must be an integer')
    if index < 0 or index >= length:
        raise CustomValueError(f'Index {index} is out of bounds for list of length {length}')

def get_element_at_position(lst, index):
    validate_index(index, len(lst))
    return lst[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_at_position(sample_list, 2))
        print(get_element_at_position(sample_list, 5))
    except (TypeError, CustomValueError) as e:
        print(e)