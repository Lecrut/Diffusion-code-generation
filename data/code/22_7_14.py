def rle_decode(compressed):
    decoded_parts = []
    i = 0
    while i < len(compressed):
        count_str = ""
        while i < len(compressed) and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        char = compressed[i]
        i += 1
        decoded_parts.append(char * count)
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_inputs = [
        "A1B2C3",
        "3A2B",
        "Z5",
        "1A2B3C",
        "Hello2World",
        "A0B1C2",
        "10A",
        "",
        "X"
    ]
    for sample in sample_inputs:
        result = rle_decode(sample)
        print(result)