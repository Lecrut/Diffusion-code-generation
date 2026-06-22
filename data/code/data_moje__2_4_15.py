def parse_volumes(input_string):
    if not input_string or input_string.strip() == "":
        return []
    parts = input_string.split(',')
    results = []
    for part in parts:
        value = part.strip()
        try:
            results.append(float(value))
        except ValueError:
            raise ValueError(f"Invalid numeric value: {value}")
    return results

if __name__ == '__main__':
    sample_input = "10.5, 20, 30.75, invalid, 40"
    try:
        output = parse_volumes(sample_input)
        print(output)
    except ValueError as e:
        print(e)