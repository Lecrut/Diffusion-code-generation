def encode(data: str) -> list:
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def decode(encoded_data: list) -> str:
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCDDDDD"
    encoded_result = encode(sample_input)
    print(encoded_result)
    decoded_result = decode(encoded_result)
    print(decoded_result)