from collections.abc import Sequence
def find_first_element(data):
    if isinstance(data, (list, tuple)):
        return data[0] if len(data) > 0 else None
    elif isinstance(data, str):
        return data[0] if len(data) > 0 else None
    elif hasattr(data, '__iter__') and not isinstance(data, (str, bytes)):
        try:
            iterator = iter(data)
            first_item = next(iterator)
            return first_item
        except StopIteration:
            return None
    elif hasattr(data, 'keys'):                                                               
        try:
            return next(iter(data.keys())) if len(data) > 0 else None
        except TypeError:
            pass
    raise TypeError(f"Unsupported data type: {type(data).__name__}. Supported types are list, tuple, str, dict_keys view.")
if __name__ == '__main__':
    samples = [
        ([10, 'hello', True], "List of mixed types"),
        ((3.5, False), "Tuple with float and bool"),
        ("python", "String input"),
        ({'a': 1}, "Dictionary keys view simulation via iter on dict_keys"),
    ]
    for test_data, description in samples:
        try:
            result = find_first_element(test_data)
            print(f"{description}: {result}")
        except TypeError as e:
            print(f"Error with {description}: {e}")