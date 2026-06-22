POSITIVE_THRESHOLD = 0.0

def _try_convert(raw_string):
    if not isinstance(raw_string, str):
        raise ValueError("Not a string")
    stripped = raw_string.strip()
    if not stripped:
        raise ValueError("Empty after strip")
    num = float(stripped)
    if num <= POSITIVE_THRESHOLD:
        raise ValueError("Not positive")
    return num

def filter_positive_weights(raw_list):
    valid = []
    for item in raw_list:
        try:
            valid.append(_try_convert(item))
        except (ValueError, TypeError):
            continue
    return valid

if __name__ == '__main__':
    test_data = ["1.5", "2", "-1", "abc", "0", "", "  3.14  ", "10"]
    print(filter_positive_weights(test_data))