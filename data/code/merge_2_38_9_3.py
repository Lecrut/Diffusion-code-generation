def yield_dict_items(source):
    for k in range(len(source)):
        if isinstance(source[k], tuple) and len(source[k]) == 2:
            yield source[k]
if __name__ == '__main__':
    data = [((1, 'a'), (3, 'c')), ((5, 'e'), (7, 'g'))]
    result_dict = {}
    for key_val in yield_dict_items(data):
        if isinstance(key_val, tuple) and len(key_val) == 2:
            k, v = key_val
            result_dict[k] = v
    print(result_dict)