def split_string(s: str, delimiter: str) -> list[str]:
    if not s:
        return []
    parts = [s]
    start = 0
    for i in range(len(s)):
        if s[i] == delimiter and (i + len(delimiter) < len(s) or s[i + len(delimiter):len(s)] != delimiter):
            end = i + len(delimiter) - 1
            while end >= start and s[end] == delimiter:
                end -= 1
            if end > start:
                parts.append(''.join(s[start:end]))
            start += 1
    return [part for part in parts if part != '']
if __name__ == '__main__':
    text = "apple,banana,cherry,date"
    result = split_string(text, ",")
    print(result)