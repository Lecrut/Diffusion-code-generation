def _validate_list(input_data):
    if not isinstance(input_data, list):
        raise ValueError("Input must be a list")
    return input_data

def check_existence(data_list):
    valid_list = _validate_list(data_list)
    if len(valid_list) == 0:
        return False
    return any(valid_list)

if __name__ == '__main__':
    samples = [
        [False, False, False],
        [False, True, False],
        [],
        [True],
        [False, False],
        [True, True, False]
    ]
    for idx, sample in enumerate(samples):
        result = check_existence(sample)
        print(result)