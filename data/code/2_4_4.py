def parse_volumes(input_string):
    parts = input_string.split(',')
    result = []
    for part in parts:
        value = part.strip()
        try:
            result.append(float(value))
        except ValueError:
            raise ValueError(f"Invalid numeric value: {value}")
    return result

if __name__ == '__main__':
    sample_input = "10.5, 20.0, 35.25"
    print(parse_volumes(sample_input))
    try:
        parse_volumes("10.5, abc, 35.25")
    except ValueError as e:
        print(e)