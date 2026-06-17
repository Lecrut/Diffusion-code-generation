def get_last_value(container: object) -> any:
    if isinstance(container, (list, tuple)) and len(container) > 0:
        return container[-1]
    elif isinstance(container, str):
        return container[-1] if container else None
    raise TypeError("Container must be a list, tuple, or string")
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    empty_tuple = ()
    full_string = "hello"
    result_list = get_last_value(sample_list) if len(sample_list) > 0 else None
    try:
        last_val = get_last_value(empty_tuple)
    except TypeError as e:
        print(f"Error with tuple: {e}")
print(result_list)