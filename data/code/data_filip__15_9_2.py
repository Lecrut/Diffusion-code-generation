from typing import Optional

def compress_string(text: str) -> Optional[str]:
    if not text:
        return text

    compressed_parts = []
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1

    compressed_parts.append(f"{current_char}{count}")
    compressed_result = "".join(compressed_parts)

    if len(compressed_result) < len(text):
        return compressed_result
    return text

if __name__ == '__main__':
    sample_input = 'aabcccccaaa'
    result = compress_string(sample_input)
    print(result)