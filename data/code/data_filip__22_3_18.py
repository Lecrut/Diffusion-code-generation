def rle_encode(data):
    if not data:
        return ""
    encoded = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        encoded.append(f"{data[i]}{count}")
        i += 1
    return "".join(encoded)

def rle_decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        char = data[i]
        i += 1
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        count = int(count_str) if count_str else 1
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDDEEEE"
    encoded_result = rle_encode(sample_string)
    decoded_result = rle_decode(encoded_result)
    print(encoded_result)
    print(decoded_result)