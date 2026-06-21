def run_length_encode(data):
    if not data:
        return ""
    encoded_parts = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_string = "AAAABBBCCDAAA"
    result = run_length_encode(sample_string)
    print(result)