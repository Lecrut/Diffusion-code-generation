def parse_delimited_string(data_string: str, delimiter: str) -> list[tuple]:
    if not data_string:
        return []
    parts = data_string.split(delimiter)
    result = []
    for part in parts:
        try:
            if delimiter == '|':
                value1_str, value2_str = part.split(':', 1)
                value1 = int(value1_str) if value1_str.isdigit() else float(value1_str)
                value2 = int(value2_str) if value2_str.isdigit() else float(value2_str)
                result.append((value1, value2))
            else:
                result.append((part,))
        except ValueError:
            result.append((part,))
    return result
if __name__ == '__main__':
    sample_data = "10|20:3.5|40:5.0|60"
    delimiter = '|'
    parsed_data = parse_delimited_string(sample_data, delimiter)
    print(parsed_data)