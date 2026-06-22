def rle_encode(input_str):
    if not input_str:
        return []
    result = []
    current_char = input_str[0]
    current_count = 1
    for i in range(1, len(input_str)):
        char = input_str[i]
        if char == current_char:
            current_count += 1
        else:
            result.append((current_char, current_count))
            current_char = char
            current_count = 1
    result.append((current_char, current_count))
    return result

if __name__ == '__main__':
    data = 'aabbaaccc'
    encoded = rle_encode(data)
    print(encoded)