def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    encoded.append(f"{current_char}{count}")
    
    return "".join(encoded)

def is_compression_effective(original: str, encoded: str) -> bool:
    return len(encoded) < len(original)

if __name__ == '__main__':
    original_string = "AAABBBCCD"
    encoded_string = run_length_encode(original_string)
    result = is_compression_effective(original_string, encoded_string)
    print(result)
    print(f"Original length: {len(original_string)}")
    print(f"Encoded length: {len(encoded_string)}")
    print(f"Encoded string: {encoded_string}")