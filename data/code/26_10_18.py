def rle_encode(input_string):
    if not input_string:
        return ""

    encoded = []
    current_char = input_string[0]
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = input_string[i]
            count = 1

    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)

    return ''.join(encoded)

if __name__ == '__main__':
    print(rle_encode("AABCCC"))
    print(rle_encode("ABC"))
    print(rle_encode("AAAA"))
    print(rle_encode(""))
    print(rle_encode("A"))
    print(rle_encode("AAABBCCC"))