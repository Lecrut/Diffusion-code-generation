class ContainerError(Exception):
    pass
def get_last_item(container: tuple | set) -> any:
    if not isinstance(container, (tuple, set)):
        raise ContainerError(f"Unsupported container type: {type(container).__name__}")
    try:
        return list(container)[-1]
    except IndexError as e:
        raise ContainerError("Container is empty") from e
if __name__ == '__main__':
    tuple_sample = (42, "hello", 3.14)
    set_sample = {7, 'world', None}
    try:
        last_tuple_item = get_last_item(tuple_sample)
        print(f"Last item in tuple: {last_tuple_item}")
        last_set_item = get_last_item(set_sample)
        print(f"Last item from set (via list): {last_set_item}")
    except ContainerError as e:
        print(f"An error occurred: {e}")
    try:
        empty_tuple = ()
        get_last_item(empty_tuple)
    except ContainerError as e:
        print(f"Expected error for empty tuple: {e}")