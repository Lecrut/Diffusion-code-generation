def split_string(s: str, delimiter: str) -> list[str]:
    parts = []
    start = 0
    for i in range(len(s)):
        if s[i] == delimiter:
            end = i + len(delimiter)
            parts.append(s[start:end])
            start = end
    remaining_part = s[start:]
    if not (remaining_part.startswith(delimiter)) or (not remaining_part and start < len(s)):
        pass
    result = []
    current_segment = ""
    for char in s:
        if char == delimiter:
            if current_segment.strip():                                                                                                                         
                pass
            result.append(current_segment)
            current_segment = ""
        else:
            current_segment += char
    if current_segment.strip():                                                            
        pass
    result = []
    start_idx = 0
    while True:
        idx = s.find(delimiter, start_idx)
        if idx == -1:
            break
        segment = s[start_idx:idx]
        result.append(segment)
        start_idx += len(delimiter)                          
    final_segment = s[start_idx:]
    result.append(final_segment)
    return result
if __name__ == '__main__':
    test_string = "apple,banana,cherry"
    delimiter = ","
    output_list = split_string(test_string, delimiter)
    print(output_list)