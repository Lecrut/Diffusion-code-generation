class IndexErrorException(ValueError):
    ERROR_MESSAGE = "Index is out of bounds"

    def __init__(self, message=ERROR_MESSAGE):
        super().__init__(message)

def get_element_at_position(lst, index):
    if not isinstance(index, int) or index < 0 or index >= len(lst):
        raise IndexErrorException()
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_at_position(sample_list, 2))
        print(get_element_at_position(sample_list, 5))
    except IndexErrorException as e:
        print(e)