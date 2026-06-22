def run_length_encode(data):
    if not data:
        return []
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
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