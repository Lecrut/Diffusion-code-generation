def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result_parts = []
    iterator = iter(data)
    try:
        current_char = next(iterator)
    except StopIteration:
        return ""
    count = 1
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result_parts.append(f"{count}{current_char}")
    return "".join(result_parts)

if __name__ == '__main__':
    sample_text = "AABBBCCCCDDDEEFFFFFF"
    encoded_output = run_length_encode(sample_text)
    print(encoded_output)