import re

def encode_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def decode_rle(data: str) -> str:
    if not data:
        return ""
    return re.sub(r'(\d+)(.)', lambda m: int(m.group(1)) * m.group(2), data)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    encoded = encode_rle(sample_text)
    decoded = decode_rle(encoded)
    print(f"Original: {sample_text}")
    print(f"Encoded:  {encoded}")
    print(f"Decoded:  {decoded}")