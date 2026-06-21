def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    count = 1
    length = len(data)
    for i in range(length):
        if i + 1 < length and data[i] == data[i + 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(data[i])
            count = 1
    return "".join(result)

def run_length_decode(encoded_data: str) -> str:
    if not encoded_data:
        return ""
    result = []
    i = 0
    length = len(encoded_data)
    while i < length:
        if not encoded_data[i].isdigit():
            raise ValueError("Invalid encoded data: missing count")
        count_str = []
        while i < length and encoded_data[i].isdigit():
            count_str.append(encoded_data[i])
            i += 1
        count = int("".join(count_str))
        if i >= length:
            raise ValueError("Invalid encoded data: missing character")
        char = encoded_data[i]
        result.append(char * count)
        i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded = run_length_encode(sample_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    large_string = "A" * 1000000 + "B" * 500000 + "C" * 250000
    large_encoded = run_length_encode(large_string)
    print(large_encoded)
    large_decoded = run_length_decode(large_encoded)
    print(len(large_decoded))
    print(large_decoded[:10] + "..." + large_decoded[-10:])