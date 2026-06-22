def run_length_encode(s: str) -> list:
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def run_length_decode(encoded: list) -> str:
    return ''.join(char * count for char, count in encoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    encoded = run_length_encode(sample_string)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)