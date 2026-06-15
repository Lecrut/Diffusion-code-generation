from typing import List, Tuple, Any
def parse_delimited_string(data_string: str, delimiter: str) -> List[Tuple[Any, ...]]:
    if not data_string:
        return []
    parts = data_string.split(delimiter)
    result = []
    for part in parts:
        if part:
            result.append(tuple(part.split(',')))
    return result
if __name__ == '__main__':
    sample_data = "1,2,3|4,5,6|7,8,9"
    delimiter = "|"
    parsed_data = parse_delimited_string(sample_data, delimiter)
    print(f"Input String: {sample_data}")
    print(f"Delimiter: '{delimiter}'")
    print("Parsed Data:")
    for item in parsed_data:
        print(item)