def decode_run_length(encoded: str) -> str:
    result = []
    i = 0
    length = len(encoded)
    while i < length:
        char = encoded[i]
        i += 1
        count_str = []
        while i < length and encoded[i].isdigit():
            count_str.append(encoded[i])
            i += 1
        count = int(''.join(count_str)) if count_str else 1
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    encoded_input = "a3b4c1d12"
    decoded_output = decode_run_length(encoded_input)
    print(decoded_output)