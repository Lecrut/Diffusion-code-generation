def parse_weight_entry(raw_input):
    text = str(raw_input).strip()
    if not text:
        raise ValueError("Empty string")
    number = float(text)
    if number <= 0:
        raise ValueError("Non-positive value")
    return number

def process_weight_measurements(input_list):
    valid_results = []
    for entry in input_list:
        try:
            result = parse_weight_entry(entry)
            valid_results.append(result)
        except (ValueError, TypeError):
            continue
    return valid_results

if __name__ == '__main__':
    test_data = ['42.0', '0.001', '-5', 'bad', '', ' 3.14 ', None, '100', '0']
    output = process_weight_measurements(test_data)
    print(output)