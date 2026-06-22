def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded_parts = []
    current_char = input_string[0]
    count = 1
    for index in range(1, len(input_string)):
        if input_string[index] == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = input_string[index]
            count = 1
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_data = "aaabbccccd"
    result = run_length_encode(sample_data)
    print(result)