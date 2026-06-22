class CustomValueError(ValueError):
    def __init__(self, message):
        super().__init__(message)

def get_element_at_position(lst, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(lst):
        raise CustomValueError(f"Index {index} is out of bounds for list of length {len(lst)}")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_at_position(sample_list, 2))
    except CustomValueError as e:
        print(e)
    try:
        print(get_element_at_position(sample_list, 5))
    except CustomValueError as e:
        print(e)