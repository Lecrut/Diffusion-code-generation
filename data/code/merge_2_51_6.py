def find_first_element(data):
    supported_types = (list, tuple, set, str)
    if isinstance(data, dict):
        try:
            keys_list = list(data.keys())
            if not keys_list:
                raise ValueError("Dictionary is empty; no element can be retrieved.")
            key_to_access = keys_list[0]
            return data[key_to_access]
        except KeyError as e:
            raise ValueError(f"Failed to access first value from dictionary: {e}")
    elif isinstance(data, supported_types):
        try:
            iterator = iter(data)
            return next(iterator)
        except StopIteration:
            raise ValueError(f"No elements found in {type(data).__name__}.")
    else:
        valid_types_str = ", ".join(t.__name__ for t in supported_types)
        raise TypeError(f"Unsupported data type '{type(data).__name__}'. Supported types are: {valid_types_str}")
if __name__ == '__main__':
    test_cases = [
        ["first", "second"],                
        (10, 20),                            
        {"a": "one"},                                                           
        "",                                           
    ]
    for i, data in enumerate(test_cases):
        try:
            result = find_first_element(data)
            print(f"Test Case {i + 1}: Input={data}, Output={result}")
        except (ValueError, TypeError) as e:
            print(f"Test Case {i + 1} Error: {e}")