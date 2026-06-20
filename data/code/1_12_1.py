def _parse_single_weight(raw_value):
    cleaned = str(raw_value).strip()
    if not cleaned:
        raise ValueError("Empty string")
    number = float(cleaned)
    if number <= 0:
        raise ValueError("Non-positive value")
    return number

def extract_positive_weights(data_list):
    results = []
    for entry in data_list:
        try:
            converted = _parse_single_weight(entry)
            results.append(converted)
        except (ValueError, TypeError):
            continue
    return results

if __name__ == '__main__':
    test_inputs = ['25.5', '  30.0  ', '-10', 'NaN', '0', 'valid', '42', '', '100']
    output_values = extract_positive_weights(test_inputs)
    print(output_values)