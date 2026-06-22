def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + input_string[i - 1])
            count = 1
    encoded.append(str(count) + input_string[-1])
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "aaabbc"
    result = run_length_encode(sample_string)
    print(result)