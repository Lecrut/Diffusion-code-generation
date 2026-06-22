def get_last_inserted_item(dictionary):
    last_key = next(reversed(dictionary))
    return last_key, dictionary[last_key]

if __name__ == '__main__':
    sample_dict = {1: 'one', 2: 'two', 3: 'three'}
    result = get_last_inserted_item(sample_dict)
    print(result)