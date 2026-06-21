def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    return "".join(encoded)

def run_length_decode(data):
    decoded = []
    i = 0
    while i < len(data):
        if data[i].isdigit():
            count_str = ""
            while i < len(data) and data[i].isdigit():
                count_str += data[i]
                i += 1
            count = int(count_str)
            if i < len(data):
                decoded.append(data[i] * count)
                i += 1
        else:
            decoded.append(data[i])
            i += 1
    return "".join(decoded)

if __name__ == "__main__":
    sample_inputs = [
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB",
        "aabbbccccd",
        "abc",
        "aaaaa",
        "aabbcc"
    ]
    for sample in sample_inputs:
        encoded = run_length_encode(sample)
        decoded = run_length_decode(encoded)
        print(f"Original: {sample}")
        print(f"Encoded: {encoded}")
        print(f"Decoded: {decoded}")
        print()