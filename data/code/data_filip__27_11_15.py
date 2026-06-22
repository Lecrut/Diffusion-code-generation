def rle_encode(text):
    if not text:
        return ""
    encoded = []
    count = 1
    current_char = text[0]
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    result = rle_encode(sample_data)
    print(result)
    empty_data = ""
    empty_result = rle_encode(empty_data)
    print(empty_result)
    single_char_data = "A"
    single_result = rle_encode(single_char_data)
    print(single_result)