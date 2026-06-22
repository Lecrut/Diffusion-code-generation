class IndexErrorException(ValueError):
    def __init__(self, message):
        super().__init__(message)

def get_element_at_position(lst, index):
    if not isinstance(index, int) or index < 0 or index >= len(lst):
        raise IndexErrorException('Index is out of bounds')
    return lst[index]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    try:
        print(get_element_at_position(sample_list, 3))
        print(get_element_at_position(sample_list, 6))
    except IndexErrorException as e:
        print(e)