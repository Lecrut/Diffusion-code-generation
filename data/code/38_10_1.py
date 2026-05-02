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
    sample_string = "programming is fun"
    repeated = find_repeated_letters(sample_string)
    print("Repeated letters found:", repeated)