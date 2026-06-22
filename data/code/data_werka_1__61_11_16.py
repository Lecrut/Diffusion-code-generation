class ElementNotFoundError(ValueError):
    def __init__(self, message):
        super().__init__(message)

def get_element_at_position(lst, index):
    if not isinstance(index, int) or index < 0 or index >= len(lst):
        raise ElementNotFoundError('Index is out of bounds')
    return lst[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        print(get_element_at_position(sample_list, 1))
        print(get_element_at_position(sample_list, 7))
    except ElementNotFoundError as e:
        print(e)