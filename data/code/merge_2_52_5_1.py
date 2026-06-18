class LastItemError(Exception):
    def __init__(self, message: str = "Cannot retrieve last item from an empty container"):
        super().__init__(message)
def get_last_item(container):
    if isinstance(container, (list, tuple)):
        try:
            return container[-1]
        except IndexError:
            raise LastItemError()
    else:
        raise TypeError("Unsupported data type. Only list and tuple are supported.")
def get_last_item_set(container):
    if isinstance(container, set):
        try:
            sorted_items = sorted(list(container))
            return sorted_items[-1]
        except IndexError:
            raise LastItemError()
    else:
        raise TypeError("Unsupported data type. Only set is supported.")
if __name__ == '__main__':
    sample_list = [5, 40, 32, 87, 99]
    sample_tuple = ('a', 'b', 'c')
    sample_set = {1, 50, 9}
    print(f"Last item in list: {get_last_item(sample_list)}")
    print(f"Last item in tuple: {get_last_item(sample_tuple)}")
    try:
        last_set_item = get_last_item_set(sample_set)
        print(f"Last item in set (max value): {last_set_item}")
    except LastItemError as e:
        pass
    try:
        raise LastItemError("Test error")
    except LastItemError as err:
        print(f"Caught expected error: {err}")