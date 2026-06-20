POSITIVE_THRESHOLD = 0

def parse_safe_numeric(raw_string):
    numeric_value = float(raw_string)
    if numeric_value <= POSITIVE_THRESHOLD:
        raise ValueError
    return numeric_value

def extract_valid_masses(measurements_list):
    collected = []
    for measurement in measurements_list:
        try:
            parsed = parse_safe_numeric(measurement)
            collected.append(parsed)
        except (ValueError, TypeError):
            continue
    return collected

if __name__ == '__main__':
    test_data = ['10.5', '5.0', '-3.2', 'invalid', '0', '7.8', '', 'abc', '12', '1e3']
    output = extract_valid_masses(test_data)
    print(output)