def find_repeated_letters(input_string):
    seen = set()
    repeated = set()
    for char in input_string:
        lower_char = char.lower()
        if 'a' <= lower_char <= 'z':
            if lower_char in seen:
                repeated.add(lower_char)
            else:
                seen.add(lower_char)
    return repeated

if __name__ == '__main__':
    sample_input_1 = "Alibaba Cloud"
    result_1 = find_repeated_letters(sample_input_1)
    print("Repeated letters in", sample_input_1, ":", result_1)

    sample_input_2 = "Python Programming"
    result_2 = find_repeated_letters(sample_input_2)
    print("Repeated letters in", sample_input_2, ":", result_2)