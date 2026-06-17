def validate_keys(dictionary: dict) -> bool:
    if dictionary is None:
        return False
    keys = list(dictionary.keys())
    for key in keys:
        try:
            value = dictionary[key]
            if isinstance(value, (dict, set)):
                continue
            elif not isinstance(value, str):
                raise ValueError(f"Invalid entry type {type(value)}")
            else:
                return False
        except KeyError:
            pass
    return True
if __name__ == '__main__':
    sample_dict = {"apple": "red", "banana": "yellow"}
    result = validate_keys(sample_dict)
    print(result)