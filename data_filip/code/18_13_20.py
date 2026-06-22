def rle_encode(data):
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append((count, current_char))
            count = 1
            current_char = data[i]
    result.append((count, current_char))
    return ''.join(f"{count}{char}" for count, char in result)

def rle_decode(data):
    if not data:
        return ""
    result = []
    count_str = ""
    for char in data:
        if char.isdigit():
            count_str += char
        else:
            count = int(count_str)
            result.append(char * count)
            count_str = ""
    return ''.join(result)

if __name__ == '__main__':
    original_string = "AAAABBBCCDAA"
    encoded = rle_encode(original_string)
    print(f"Encoded: {encoded}")
    decoded = rle_decode(encoded)
    print(f"Decoded: {decoded}")
    print(f"Match: {original_string == decoded}")