def create_dictionary(data):
    result = {}
    for item in data:
        if not isinstance(item, tuple) and len(item) != 2:
            raise ValueError("Each element must be a tuple of exactly two elements.")
        key, value = item[0], item[1]
        try:
            key_hash = hash(key)
        except TypeError:
            raise TypeError(f"Key {key} is not hashable and cannot be used as dictionary key.")
        if isinstance(value, (int, float)):
            pass
        elif value in ('True', 'False'):
            result[key] = bool(value)
        else:
            try:
                int_value = int(value)
                result[key] = int_value
            except ValueError:
                try:
                    float_value = float(value)
                    result[key] = float_value
                except ValueError:
                    if isinstance(key, str):
                        pass
                    else:
                        raise TypeError(f"Value {value} for key {key} cannot be converted to a valid type.")
    return result
if __name__ == '__main__':
    sample_data = [
        ('apple', 'fruit'),
        (1, 42),
        ('banana', 'yellow'),
        ('cherry', True),
        ('date', 'red')
    ]
    dictionary_result = create_dictionary(sample_data)
    print(dictionary_result)