def decode_rle(encoded_string):
    if not encoded_string:
        return ""
    result = []
    i = 0
    n = len(encoded_string)
    while i < n:
        if encoded_string[i].isdigit():
            start = i
            while i < n and encoded_string[i].isdigit():
                i += 1
            count = int(encoded_string[start:i])
            if i >= n or not encoded_string[i].isalpha():
                raise ValueError("Invalid RLE format: character missing after count")
            char = encoded_string[i]
            i += 1
            result.append(char * count)
        elif encoded_string[i].isalpha():
            result.append(encoded_string[i])
            i += 1
        else:
            raise ValueError(f"Invalid character '{encoded_string[i]}' in encoded string")
    return "".join(result)

if __name__ == '__main__':
    sample1 = "12A3B2C"
    sample2 = "4Z5W10X"
    sample3 = "A3B2"
    sample4 = "123A"
    print(decode_rle(sample1))
    print(decode_rle(sample2))
    print(decode_rle(sample3))
    print(decode_rle(sample4))
    try:
        decode_rle("3G")
    except ValueError as e:
        print(e)
    try:
        decode_rle("A3B")
    except ValueError as e:
        print(e)
    try:
        decode_rle("12!")
    except ValueError as e:
        print(e)