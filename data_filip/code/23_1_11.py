def run_length_encode(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = char
            count = 1
    result.append((count, current_char))
    return result

def run_length_decode(data):
    return [char * count for count, char in data]

if __name__ == '__main__':
    sample_input = "aaabbbccccdddd"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)