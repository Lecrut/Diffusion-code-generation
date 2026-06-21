def run_length_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    start = 0
    length = len(text)
    while start < length:
        char = text[start]
        end = start + 1
        while end < length and text[end] == char:
            end += 1
        count = end - start
        result.append(f"{char}{count}")
        start = end
    return "".join(result)

if __name__ == '__main__':
    sample_text = 'wwwwaaadexxxxxx'
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)