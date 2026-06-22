def rle_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 255:
            count += 1
        else:
            encoded.append("{}{}".format(count, current_char))
            current_char = char
            count = 1
    encoded.append("{}{}".format(count, current_char))
    return "".join(encoded)

def rle_decode(data):
    decoded = []
    i = 0
    while i < len(data):
        count = 0
        while i < len(data) and data[i].isdigit():
            count = count * 10 + int(data[i])
            i += 1
        if i < len(data):
            char = data[i]
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_text = "AAABBBCCCCDDDDDEEEEFFFFFFGGHHHIIIIJJJKKKLMMNNNOOOOPPQQQRRRSSSSTTTTUUUUVVVVWWWXXXYYYZZZ"
    encoded = rle_encode(sample_text)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)
    print(sample_text == decoded)