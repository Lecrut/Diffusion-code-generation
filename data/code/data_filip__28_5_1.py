def run_length_encode(text):
    if not text:
        return ""
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

def run_length_decode(encoded):
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return "".join(decoded)

def verify_rle_roundtrip(original_text):
    encoded = run_length_encode(original_text)
    decoded = run_length_decode(encoded)
    return decoded == original_text

if __name__ == '__main__':
    sample_text = "aaabbcdddde"
    result = verify_rle_roundtrip(sample_text)
    print(result)