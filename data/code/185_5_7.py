def parse_delimited_string(data_string: str, delimiter: str) -> list[tuple]:
    if not data_string:
        return []
    parts = data_string.split(delimiter)
    result = []
    for part in parts:
        try:
            value = int(part)
            result.append((value,))
        except ValueError:
            result.append((part,))
    return result
if __name__ == '__main__':
    sample_string = "10|25|33|42"
    delimiter = "|"
    parsed_data = parse_delimited_string(sample_string, delimiter)
    print(parsed_data)