from typing import Optional

def compress_string(text: str) -> Optional[str]:
    if not text:
        return ""
    compressed_chars = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed_chars.append(f"{current_char}{count}")
            current_char = text[i]
            count = 1
    compressed_chars.append(f"{current_char}{count}")
    compressed_string = "".join(compressed_chars)
    if len(compressed_string) < len(text):
        return compressed_string
    return None

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = compress_string(sample_input)
    print(result)