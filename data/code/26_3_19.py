def encode_rle(text):
    if not text:
        return ""
    encoded_parts = []
    index = 0
    while index < len(text):
        current_symbol = text[index]
        run_length = 0
        while index < len(text) and text[index] == current_symbol:
            run_length += 1
            index += 1
        encoded_parts.append(f"{run_length}{current_symbol}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    input_data = "XXYYYYZ"
    output_text = encode_rle(input_data)
    print(output_text)