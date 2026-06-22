def run_length_encode(input_string):
    if not input_string:
        return []

    encoded = []
    current_char = input_string[0]
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = input_string[i]
            count = 1

    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample1 = "AAABBBCCDAA"
    print(run_length_encode(sample1))

    sample2 = "abc"
    print(run_length_encode(sample2))

    sample3 = ""
    print(run_length_encode(sample3))

    sample4 = "AAAAA"
    print(run_length_encode(sample4))

    sample5 = "AABBCCDDEEFF"
    print(run_length_encode(sample5))