def run_length_encode(data):
    if not data:
        return []
    encoded = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample = 'AAAABBBCCDAA'
    result = run_length_encode(sample)
    print(result)