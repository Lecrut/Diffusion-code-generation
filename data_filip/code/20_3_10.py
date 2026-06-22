def run_length_encode(text):
    if not text:
        return ''
    encoded = []
    count = 1
    current_char = text[0]
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return ''.join(encoded)

if __name__ == '__main__':
    sample = "AAABBBCCD"
    print(run_length_encode(sample))