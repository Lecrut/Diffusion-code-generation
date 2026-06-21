def run_length_encode(source):
    if not source:
        return ""
    encoded_chars = []
    current_char = source[0]
    count = 1
    for char in source[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_chars.append((current_char, count))
            current_char = char
            count = 1
    encoded_chars.append((current_char, count))
    return "".join(f"{char}{count}" for char, count in encoded_chars)

def run_length_decode(encoded):
    if not encoded:
        return ""
    decoded_chars = []
    i = 0
    while i < len(encoded):
        if not encoded[i].isalpha():
            i += 1
            continue
        char = encoded[i]
        i += 1
        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        count = int(count_str) if count_str else 1
        decoded_chars.append(char * count)
    return "".join(decoded_chars)

if __name__ == '__main__':
    sample1 = "AAABBBCCCCA"
    encoded1 = run_length_encode(sample1)
    decoded1 = run_length_decode(encoded1)
    print(f"Original: {sample1}")
    print(f"Encoded: {encoded1}")
    print(f"Decoded: {decoded1}")

    sample2 = "abbbcccaa"
    encoded2 = run_length_encode(sample2)
    decoded2 = run_length_decode(encoded2)
    print(f"Original: {sample2}")
    print(f"Encoded: {encoded2}")
    print(f"Decoded: {decoded2}")

    sample3 = ""
    encoded3 = run_length_encode(sample3)
    decoded3 = run_length_decode(encoded3)
    print(f"Original: {sample3}")
    print(f"Encoded: {encoded3}")
    print(f"Decoded: {decoded3}")

    sample4 = "Z"
    encoded4 = run_length_encode(sample4)
    decoded4 = run_length_decode(encoded4)
    print(f"Original: {sample4}")
    print(f"Encoded: {encoded4}")
    print(f"Decoded: {decoded4}")