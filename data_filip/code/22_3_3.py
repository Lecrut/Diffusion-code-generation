def rle_encode(data):
    if not data:
        return ""
    encoding = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoding.append(str(count) + data[i - 1])
            count = 1
    encoding.append(str(count) + data[-1])
    return "".join(encoding)

def rle_decode(data):
    decoding = []
    count = ""
    for char in data:
        if char.isdigit():
            count += char
        else:
            decoding.append(char * int(count))
            count = ""
    return "".join(decoding)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_value = rle_encode(sample_string)
    decoded_value = rle_decode(encoded_value)
    print(encoded_value)
    print(decoded_value)