def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded_parts = []
    count = 1
    length = len(input_string)
    for i in range(length):
        if i < length - 1 and input_string[i] == input_string[i + 1]:
            count += 1
        else:
            encoded_parts.append(str(count))
            encoded_parts.append(input_string[i])
            count = 1
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_input = "aaabbbcccaaa"
    result = run_length_encode(sample_input)
    print(result)