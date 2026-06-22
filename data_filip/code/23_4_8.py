def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded.append(text[i - 1])
            if count > 1:
                encoded.append(str(count))
            count = 1
    encoded.append(text[-1])
    if count > 1:
        encoded.append(str(count))
    return "".join(encoded)

def run_length_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        count = int(num_str) if num_str else 1
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    samples = [
        "aaabccccde",
        "abcd",
        "a",
        "",
        "aaabbbaaa",
        "aabbccdd",
        "aaaaa"
    ]
    for sample in samples:
        encoded = run_length_encode(sample)
        decoded = run_length_decode(encoded)
        print(f"Original: '{sample}'")
        print(f"Encoded: '{encoded}'")
        print(f"Decoded: '{decoded}'")
        print("---")