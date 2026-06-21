def retrieve_elements(nested_dict, keys):
    result = {}
    for key in keys:
        current_level = nested_dict
        for sub_key in key.split('.'):
            if sub_key in current_level:
                current_level = current_level[sub_key]
            else:
                return None
        result[key] = current_level
    return result

if __name__ == '__main__':
    sample_data = {
        'level1': {
            'level2a': {
                'level3a': 42,
                'level3b': 78
            },
            'level2b': {
                'level3c': 99
            }
        },
        'level1b': {
            'level2c': {
                'level3d': 101
            }
        }
    }

    keys_to_retrieve = ['level1.level2a.level3a', 'level1.level2b.level3c', 'level1b.level2c.level3d']
    retrieved_elements = retrieve_elements(sample_data, keys_to_retrieve)
    print(retrieved_elements)