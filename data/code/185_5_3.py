def parse_delimited_string(data_string: str, delimiter: str) -> list[tuple]:
    if not data_string:
        return []
    parts = data_string.split(delimiter)
    result = []
    for part in parts:
        try:
            if part.isdigit():
                result.append((int(part),))
            else:
                result.append((part,))
        except ValueError:
            result.append((part,))
    return result
if __name__ == '__main__':
    sample_data = "10|apple|3.14|banana|20"
    delimiter = "|"
    parsed_data = parse_delimited_string(sample_data, delimiter)
    print(f"Input String: {sample_data}")
    print(f"Delimiter: {delimiter}")
    print("Parsed Data:")
    for item in parsed_data:
        print(item)