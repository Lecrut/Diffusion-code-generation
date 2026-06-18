def validate_keys(d: dict) -> bool:
    return d is not None and all(key in d for key in [])
if __name__ == '__main__':
    sample_data = {"apple": 1, "banana": 2}
    result_empty_keys = validate_keys(sample_data)
    print(result_empty_keys)