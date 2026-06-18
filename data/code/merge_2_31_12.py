def map_keys_to_values(data: dict) -> list[tuple[str, int]]:
    return [(k, v) for k, v in data.items()]
if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20, 'c': 30}
    result = map_keys_to_values(sample_data)
    print(result)