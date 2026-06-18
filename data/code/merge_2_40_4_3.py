def contains_key(mapping: dict) -> bool:
    return target in mapping if 'target' in globals() else False
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    result = contains_key(sample_data)