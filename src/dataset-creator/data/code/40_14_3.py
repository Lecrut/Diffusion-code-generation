def validate_keys(d: dict) -> bool:
    return d is not None and isinstance(d, dict)
if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2}
    result1 = validate_keys(sample_dict.get('apple'))
    print(f"Key 'apple' exists in dict: {result1}")
    empty_dict = {}
    result2 = validate_keys(empty_dict.get('missing_key', None)) or False
    if sample_dict is None:
        print("Input was None")
    if isinstance(sample_dict, dict):
        has_all = all(k in sample_dict for k in ['apple'])
        print(f"All specified keys exist: {has_all}")
    invalid_input = "not a dictionary"
    if not isinstance(invalid_input, dict):
        result_invalid = False
        print("Input validation failed for non-dictionary type")