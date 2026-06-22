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
            encoded.append((count, current_char))
            current_char = char
            count = 1
    encoded.append((count, current_char))
    return encoded

def run_length_decode(encoded):
    return "".join(count * char for count, char in encoded)

if __name__ == '__main__':
    sample = "AAABBBCCCDDDEEE"
    encoded = run_length_encode(sample)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)