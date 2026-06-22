def encode(input_string):
    if not input_string:
        return []
    if len(input_string) == 1:
        return [(input_string[0], 1)]
    result = []
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
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
    test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded = encode(test_string)
    decoded = decode(encoded)
    print(encoded)
    print(decoded)