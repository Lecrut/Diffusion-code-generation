def extract_elements(nested_dict, keys):
    def validate_keys(keys):
        if not all(isinstance(k, str) for k in keys):
            raise ValueError("All keys must be strings")
    
    validate_keys(keys)
    
    result = {}
    for key in keys:
        parts = key.split('.')
        value = nested_dict
        for part in parts:
            if isinstance(value, dict):
                value = value.get(part, None)
            else:
                value = None
                break
        result[key] = value
    
    return result

if __name__ == '__main__':
    sample_data = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3,
                'f': 4
            }
        },
        'g': {
            'h': 5,
            'i': 6
        }
    }
    
    keys = ['a', 'b.c', 'b.d.e', 'g.h.i']
    extracted_values = extract_elements(sample_data, keys)
    print(extracted_values)