def numeric_to_text(key_map):

    def convert_key(key):
        return key_map.get(key, 'Unknown')
    return convert_key
if __name__ == '__main__':
    sample_mapping = {1: 'One', 2: 'Two', 3: 'Three'}
    converter = numeric_to_text(sample_mapping)
    print(converter(2))
    print(converter(4))