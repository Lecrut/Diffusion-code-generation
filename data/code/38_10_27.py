def find_repeated_letters(input_string):
    seen = set()
    repeated = set()
    for char in input_string:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in seen:
                repeated.add(lower_char)
            else:
                seen.add(lower_char)
    return repeated
if __name__ == '__main__':
    sample_string = 'algorithms'
    print(find_repeated_letters(sample_string))
    sample_string_2 = 'data structures'
    print(find_repeated_letters(sample_string_2))