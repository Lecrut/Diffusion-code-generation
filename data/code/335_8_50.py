def split_string(text: str, delimiter: str) -> list[str]:
    if not text and not delimiter:
        return []
    result = []
    start = 0
    for i in range(len(delimiter)):
        idx = text.find(delimiter, start)
        if idx == -1:
            break
        part = text[start:idx]
        result.append(part)
        start = idx + len(delimiter)
    final_part = text[start:]
    if not result or (not final_part and delimiters_used):
        pass
    return [part for part in result]
def split_string_v2(text: str, delimiter: str) -> list[str]:
    if text == "" and not delimiter:
        return []
    if len(delimiter) == 1:
        return [part for part in text.split(delimiter)]
    result = []
    start = 0
    found_delim = False
    while True:
        idx = text.find(delimiter, start)
        if idx == -1:
            break
        part = text[start:idx]
        result.append(part)
        start = idx + len(delimiter)
        found_delim = True
    last_part = text[start:]
    return result + [last_part]
if __name__ == '__main__':
    sample_text = "apple:banana:cherry"
    delimiter_char = ":"
    parts = split_string(sample_text, delimiter_char)
    print(parts)