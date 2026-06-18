def split_string(s: str, delimiter: str) -> list[str]:
    result = []
    start = 0
    while True:
        index = s.find(delimiter, start)
        if index == -1:
            remaining_part = s[start:]
            if len(remaining_part.strip()) > 0 or (len(result) == 0 and not delimiter):
                result.append(s[start:])
            break
        else:
            part = s[start:index]
            result.append(part)
            start = index + 1
    return result
if __name__ == '__main__':
    sample_string = "apple,banana,cherry"
    delimiter = ","
    parts = split_string(sample_string, delimiter)
    print(parts)