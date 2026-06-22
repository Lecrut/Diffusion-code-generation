VALID_POSITIVE_THRESHOLD = 0.0

def _is_valid_positive_weight(raw_string):
    stripped = str(raw_string).strip()
    if not stripped:
        raise ValueError("Empty input")
    parsed_value = float(stripped)
    if parsed_value <= VALID_POSITIVE_THRESHOLD:
        raise ValueError("Non-positive value")
    return parsed_value

def extract_valid_weights(weight_list):
    collected = []
    for item in weight_list:
        try:
            valid_number = _is_valid_positive_weight(item)
            collected.append(valid_number)
        except (ValueError, TypeError):
            continue
    return collected

if __name__ == '__main__':
    test_data = ['10.5', '5.0', '-3.2', 'invalid', '0', '7.8', '', 'abc', '12', '  4.2  ', None]
    output = extract_valid_weights(test_data)
    print(output)