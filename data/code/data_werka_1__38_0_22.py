def find_repeated_letters(input_string):
    def is_letter(char):
        return 'a' <= char.lower() <= 'z'

    seen = set()
    repeated = set()

    for char in input_string:
        if is_letter(char):
            if char in seen:
                repeated.add(char)
            else:
                seen.add(char)

    return sorted(list(repeated))

if __name__ == '__main__':
    sample_input_1 = "repetition"
    sample_input_2 = "unique"
    
    result_1 = find_repeated_letters(sample_input_1)
    result_2 = find_repeated_letters(sample_input_2)
    
    print("Repeated letters in '{}': {}".format(sample_input_1, result_1))
    print("Repeated letters in '{}': {}".format(sample_input_2, result_2))