def parse_volumes(input_string):
    parts = input_string.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped == '':
            continue
        try:
            value = float(stripped)
            result.append(value)
        except ValueError:
            result.append(float('nan'))
    return result

if __name__ == '__main__':
    sample_input = "1.5, 2.3, abc, 4.0, , 5.1"
    parsed = parse_volumes(sample_input)
    print(parsed)