def retrieve_nested_value(data, keys):
    try:
        current = data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            elif isinstance(current, list) and isinstance(key, int) and (0 <= key < len(current)):
                current = current[key]
            else:
                raise KeyError(f"Key '{key}' not found")
        return current
    except (KeyError, TypeError):
        raise ValueError('Invalid keys or data structure')
if __name__ == '__main__':
    SAMPLE_DATA = {'a': {'b': {'c': 42, 'd': 'hello'}, 'e': [1, 2, 3]}, 'f': True, 'g': [{'h': 1}, {'i': 2}]}
    KEYS_TO_RETRIEVE_1 = ['a', 'b', 'c']
    KEYS_TO_RETRIEVE_2 = ['a', 'e', 1]
    KEYS_TO_RETRIEVE_3 = ['g', 0, 'h']
    print(retrieve_nested_value(SAMPLE_DATA, KEYS_TO_RETRIEVE_1))
    print(retrieve_nested_value(SAMPLE_DATA, KEYS_TO_RETRIEVE_2))
    print(retrieve_nested_value(SAMPLE_DATA, KEYS_TO_RETRIEVE_3))