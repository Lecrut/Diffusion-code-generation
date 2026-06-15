def parse_delimited_string(data_string: str, delimiter: str) -> list[tuple]:
    if not data_string:
        return []
    parts = data_string.split(delimiter)
    result = []
    for part in parts:
        try:
            if part:
                result.append((int(part),))
        except ValueError:
            result.append((part,))
    return result
if __name__ == '__main__':
    sample_data = "10|25|33|42"
    delimiter = "|"
    parsed_data = parse_delimited_string(sample_data, delimiter)
    print(f"Input String: {sample_data}")
    print(f"Delimiter: {delimiter}")
    print("Parsed Data (List of Tuples):")
    print(parsed_data)
    sample_data_mixed = "10.5|25|33.1"
    parsed_data_mixed = parse_delimited_string(sample_data_mixed, "|")
    print("\n--- Mixed Data Example ---")
    print(f"Input String: {sample_data_mixed}")
    print("Parsed Data (List of Tuples):")
    print(parsed_data_mixed)