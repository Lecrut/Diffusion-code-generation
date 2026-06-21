def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

def run_length_decode(encoded_text):
    decoded = []
    i = 0
    while i < len(encoded_text):
        char = encoded_text[i]
        i += 1
        num_str = ""
        while i < len(encoded_text) and encoded_text[i].isdigit():
            num_str += encoded_text[i]
            i += 1
        count = int(num_str)
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == "__main__":
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = run_length_encode(sample_input)
    decoded_result = run_length_decode(encoded_result)
    print(sample_input == decoded_result)