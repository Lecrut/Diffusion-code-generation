def get_last_key_value(data):
    if not data:
        return None
    last_item = list(data.items())[-1]
    return last_item

if __name__ == '__main__':
    sample_dict = {'first': 1, 'second': 2, 'third': 3}
    result = get_last_key_value(sample_dict)
    print(result)