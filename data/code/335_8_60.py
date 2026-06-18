def split_string(s: str, delimiter: str) -> list[str]:
    result = []
    start = 0
    for i in range(len(s)):
        if s[i] == delimiter:
            part = s[start:i]
            if part or (i + 1 < len(s) and not any(c == delimiter for c in s[i+1:])):
                result.append(part)
            start = i + 1
    return [s[start:].strip() if s.startswith(delimiter) else s[start:]]
def split_string_v2(s: str, delimiter: str) -> list[str]:
    parts = []
    current_part = ""
    for char in s:
        if char == delimiter:
            if current_part or (len(parts) > 0 and not any(p.strip() == '' for p in parts)):
                parts.append(current_part.strip())
            current_part = ""
        else:
            current_part += char
    if current_part:
        parts.append(current_part.strip())
    return [p for p in parts if len(p) > 0]
if __name__ == '__main__':
    test_string = "apple,banana,cherry"
    delimiter = ","
    result = split_string_v2(test_string, delimiter)
    print(result)