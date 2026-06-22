def encode_rle(input_string):
    if not input_string:
        return ""
    result = []
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample = "aaabbc"
    print(encode_rle(sample))
    sample_empty = ""
    print(encode_rle(sample_empty))
    sample_single = "x"
    print(encode_rle(sample_single))
    sample_mixed = "hello"
    print(encode_rle(sample_mixed))
    sample_repeated = "pppppp"
    print(encode_rle(sample_repeated))