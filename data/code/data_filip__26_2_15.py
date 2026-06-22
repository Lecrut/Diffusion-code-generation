def run_length_encode(text: str) -> list[tuple[str, int]]:
    if not text:
        return []
    encoded = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = text[i]
            count = 1
    encoded.append((current_char, count))
    return encoded
if __name__ == '__main__':
    sample_strings = ['AABCCCCCAAB', 'ABC', '', 'AAAAA']
    for s in sample_strings:
        result = run_length_encode(s)
        print(result)