def encode_run_length(data: str) -> str:
    if not data:
        return ""
    result = []
    length = len(data)
    i = 0
    while i < length:
        current_char = data[i]
        count = 1
        i += 1
        while i < length and data[i] == current_char:
            count += 1
            i += 1
        result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    encoded_result = encode_run_length(sample_string)
    print(encoded_result)
    sample_string_empty = ""
    print(encode_run_length(sample_string_empty))
    sample_string_single = "A"
    print(encode_run_length(sample_string_single))
    sample_string_mixed = "AAABBBCCCC"
    print(encode_run_length(sample_string_mixed))