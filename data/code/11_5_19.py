def get_last_item(sequence):
    if not sequence:
        return None
    result = None
    for value in sequence:
        result = value
    return result

ITEM_TYPES = {
    'int': int,
    'str': str,
    'float': float,
    'list': list
}

if __name__ == '__main__':
    sample_data = [42, 17, 9, 3]
    final_value = get_last_item(sample_data)
    print(final_value)
    empty_data = []
    empty_value = get_last_item(empty_data)
    print(empty_value)
    mapped_type = ITEM_TYPES.get('int', lambda x: x)
    print(mapped_type(100))