def split_and_trim(s: str) -> list:
    if not s:
        return []
    result = []
    for part in s.split(','):
        trimmed = part.strip()
        if trimmed:
            result.append(trimmed)
    return result

if __name__ == '__main__':
    sample_input = "  apple , banana,  orange ,  , grape  , "
    print(split_and_trim(sample_input))