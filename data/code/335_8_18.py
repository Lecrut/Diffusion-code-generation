def split_string(text: str, delimiter: str) -> list[str]:
    result = []
    start = 0
    for i in range(len(text)):
        if text[i] == delimiter:
            end = i + len(delimiter)
            part = text[start:end].strip()
            if part:
                result.append(part)
            start = end
    final_part = text[start:].strip()
    if final_part:
        result.append(final_part)
    return result
if __name__ == '__main__':
    sample_text = "apple,banana,cherry,date"
    delimiter = ","
    parts = split_string(sample_text, delimiter)
    print("Split Result:")
    for i, part in enumerate(parts):
        print(f"{i}: {part}")