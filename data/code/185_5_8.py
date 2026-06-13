def parse_delimited_string(data_string: str, delimiter: str) -> list[tuple]:
    if not data_string:
        return []
    parts = data_string.split(delimiter)
    result = []
    for part in parts:
        try:
            value = int(part.strip())
            result.append((value,))
        except ValueError:
            result.append((part.strip(),))
    return result
if __name__ == '__main__':
    sample_data = "10|25|33|42"
    delimiter = "|"
    parsed_data = parse_delimited_string(sample_data, delimiter)
    print(parsed_data)
    sample_data_mixed = "10|hello|33|world"
    parsed_data_mixed = parse_delimited_string(sample_data_mixed, delimiter)
    print(parsed_data_mixed)
    sample_data_empty = ""
    parsed_data_empty = parse_delimited_string(sample_data_empty, delimiter)
    print(parsed_data_empty)