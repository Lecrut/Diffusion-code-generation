def map_keys_to_values(data: dict) -> list[tuple[str, str]]:
    return [(k, v) for k, v in data.items() if isinstance(v, (str, int))]
if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 'hello', 'c': None}
    result = map_keys_to_values(sample_data)
    print(result)