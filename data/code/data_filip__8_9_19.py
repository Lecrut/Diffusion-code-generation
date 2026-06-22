def split_and_trim(text: str) -> list[str]:
    if not text:
        return []
    parts = text.split(',')
    result = []
    for part in parts:
        trimmed = part.strip()
        if trimmed:
            result.append(trimmed)
    return result

if __name__ == '__main__':
    sample_data = "  apple , banana,  ,orange,  grape  , "
    output = split_and_trim(sample_data)
    print(output)