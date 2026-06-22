NUMBERS = {
    'group_a': [7, 42, 15],
    'group_b': [100, 200, 300]
}

def extract_first_value(mapping, key):
    target_list = mapping[key]
    return target_list[0]

if __name__ == '__main__':
    sample_key = 'group_a'
    first_item = extract_first_value(NUMBERS, sample_key)
    print(first_item)