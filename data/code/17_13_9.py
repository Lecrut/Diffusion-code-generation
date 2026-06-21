def get_last_item(d):
    if not d:
        return None
    last_key = next(reversed(d))
    return (last_key, d[last_key])

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(get_last_item(sample_dict))