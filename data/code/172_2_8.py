def numeric_to_text(key_map):
    def convert_key(key):
        return key_map.get(key, 'Unknown')
    return {key: convert_key(key) for key in key_map.keys()}

if __name__ == '__main__':
    sample_mapping = {1: 'One', 2: 'Two', 3: 'Three'}
    converted_values = numeric_to_text(sample_mapping)
    print(converted_values)