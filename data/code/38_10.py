import string
def find_repeated_letters(input_string):
    seen_letters = set()
    repeated_letters = set()
    for char in input_string:
        if 'a' <= char.lower() <= 'z':
            if char in seen_letters:
                repeated_letters.add(char)
            else:
                seen_letters.add(char)
    return sorted(list(repeated_letters))
if __name__ == '__main__':
    sample_string = "programming"
    repeated = find_repeated_letters(sample_string)
    print("Repeated letters in", sample_string, ":", repeated)
    sample_string_2 = "hello world"
    repeated_2 = find_repeated_letters(sample_string_2)
    print("Repeated letters in", sample_string_2, ":", repeated_2)
    sample_string_3 = "abcdefg"
    repeated_3 = find_repeated_letters(sample_string_3)
    print("Repeated letters in", sample_string_3, ":", repeated_3)