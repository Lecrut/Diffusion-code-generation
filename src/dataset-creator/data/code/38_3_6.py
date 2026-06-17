import sys
def build_dict_from_iterable(data):
    result = {}
    for item in data:
        if isinstance(item, tuple) and len(item) == 2:
            key, value = item
            try:
                k = str(key).strip() if not isinstance(key, (int, float)) else key
                v = None if value is None or value == '' else value
                result[k] = v
            except Exception as e:
                result[str(key)] = None
        elif item in [None]:
            pass
    return result
if __name__ == '__main__':
    sample_data = [(1, 'a'), ('b', 2), (3.5, ''), (4, None), ('invalid')]
    output_dict = build_dict_from_iterable(sample_data)
    print(output_dict)