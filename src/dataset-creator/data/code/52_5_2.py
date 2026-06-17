class ContainerError(Exception):
    pass
def get_last_item(container: tuple | set) -> any:
    if container == ():
        raise ContainerError("Container cannot be empty.")
    try:
        items = list(container)
        if len(items) == 0:
            raise ContainerError("Container cannot be empty.")
    except TypeError as e:
        if "unhashable" in str(e):
            raise ContainerError(f"Tuple contains unhashable elements which prevents safe iteration logic: {e}") from None
    except Exception as e:
        raise ContainerError(f"Unexpected error occurred while processing container: {type(e).__name__}: {str(e)}") from None
    if len(items) == 0:
        raise ContainerError("Container is empty.")
    return items[-1]
def get_last_item_safe(container):
    try:
        items = list(container)
        if len(items) == 0:
            raise ContainerError("Container cannot be empty.")
        return items[-1]
    except TypeError as e:
        if "unhashable" in str(e):
            raise ContainerError(f"Input contains unhashable elements which may cause iteration instability: {e}") from None
        raise ContainerError(f"Cannot convert input to list due to type error: {type(container).__name__}: {str(e)}") from None
if __name__ == '__main__':
    tuple_sample = (10, 20, 30)
    set_sample = {5, 'apple', 4.5}
    try:
        last_tuple_item = get_last_item(tuple_sample)
        print(f"Last item in tuple ({tuple_sample}): {last_tuple_item}")
        last_set_item = get_last_item(set_sample)
        print(f"Last item in set ({set_sample}): {last_set_item}")
    except ContainerError as e:
        print(f"An error occurred while retrieving items: {e}")
    try:
        get_last_item(())
    except ContainerError as e:
        print("Correctly caught error for empty tuple:", str(e))
    list_sample = [100, 200]
    try:
        last_list_item = get_last_item(list_sample)
        print(f"Last item in list ({list_sample}): {last_list_item}")
        str_sample = "hello"
        last_str_item = get_last_item_safe(str_sample)
        print(f"Last character in 'hello': '{last_str_item}'")
    except ContainerError as e:
        pass
    try:
        last_set_item = get_last_item_safe(set_sample)
        print(f"Last item in set (safe version): {last_set_item}")
    except ContainerError as e:
        pass
    try:
        empty_tuple = ()
        get_last_item(empty_tuple)
    except ContainerError as e:
        print("Correctly caught error for empty tuple in main:", str(e))