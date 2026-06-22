def run_length_encode(input_string):
    if not input_string:
        return ""
    normalized_string = input_string.lower()
    encoded_parts = []
    current_char = normalized_string[0]
    count = 1
    for i in range(1, len(normalized_string)):
        if normalized_string[i] == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = normalized_string[i]
            count = 1
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "AaaBBbCCCdDdEe"
    result = run_length_encode(sample_input)
    print(result)