def encode(data):
    if not data:
        return []
    result = []
    iterator = iter(data)
    current_char = next(iterator)
    count = 1
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def decode(encoded_list):
    result = []
    for char, count in encoded_list:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample = "aaabbbccc"
    encoded = encode(sample)
    print(encoded)
    decoded = decode(encoded)
    print(decoded)