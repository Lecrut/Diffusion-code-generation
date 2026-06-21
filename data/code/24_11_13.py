def run_length_encode(input_string):
    if not input_string:
        return ""
    compressed = []
    current_char = input_string[0]
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            if count > 1:
                compressed.append(str(count))
            current_char = input_string[i]
            count = 1
    compressed.append(current_char)
    if count > 1:
        compressed.append(str(count))
    return "".join(compressed)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDE"
    result = run_length_encode(sample_input)
    print(result)
    another_sample = "XYZ"
    print(run_length_encode(another_sample))
    empty_sample = ""
    print(run_length_encode(empty_sample))