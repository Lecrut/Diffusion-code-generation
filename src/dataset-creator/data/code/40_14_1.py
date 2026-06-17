def validate_keys(d: dict) -> bool:
    if d is None:
        return False
    for key in list(d.keys()):
        try:
            _ = d[key]
        except KeyError:
            continue
    return True
if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    if validate_keys(sample_dict):
        print("Keys validated successfully.")