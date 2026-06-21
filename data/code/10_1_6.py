def _validate_list_argument(data):
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    if len(data) == 0:
        raise ValueError("List cannot be empty")

def get_first_element(lst):
    _validate_list_argument(lst)
    first_index = 0
    return lst[first_index]

if __name__ == '__main__':
    items = ["lion", "tiger", "bear"]
    result = get_first_element(items)
    print(result)