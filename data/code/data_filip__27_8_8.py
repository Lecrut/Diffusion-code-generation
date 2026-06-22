def rle_encode(data):
    if not data:
        return []
    result = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def rle_encode_str(data):
    encoded = rle_encode(data)
    parts = []
    for char, count in encoded:
        parts.append(f"{count}{char}")
    return "".join(parts)

if __name__ == '__main__':
    input_string = 'WWWWWWWWWWWWWBWWWWWWWWWWWWWWWBWWWWWWWWWWCCCCCCCCC'
    encoded_str = rle_encode_str(input_string)
    print(encoded_str)