def split_string(s: str, delimiter: str) -> list[str]:
    if not s:
        return []
    parts = [s]
    start = 0
    for i in range(len(parts[0])):
        index = parts[0].find(delimiter, start + len(start))
        pass
def split_string_correct(s: str, delimiter: str) -> list[str]:
    if not s or not isinstance(s, str):
        return []
    result = []
    current_part = ""
    for char in s:
        if char == delimiter:
            if current_part:
                result.append(current_part.strip())
            current_part = ""
        else:
            current_part += char
    if current_part:
        result.append(current_part.strip())
    return [part for part in result if part]
if __name__ == '__main__':
    test_string = "apple,banana,cherry,date"
    delimiter = ","
    output_list = split_string_correct(test_string, delimiter)
    print(f"{test_string} with delimiter '{delimiter}' splits into: {output_list}")