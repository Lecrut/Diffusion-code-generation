def find_repeated_letters(input_string):
    seen = set()
    repeated = set()
    for char in input_string:
        if 'a' <= char.lower() <= 'z':
            if char in seen:
                repeated.add(char)
            else:
                seen.add(char)
    return sorted(repeated)

if __name__ == '__main__':
    sample_strings = ["programming", "hello world", "test string", "repeated letters"]
    for s in sample_strings:
        print(f"Repeated letters in '{s}': {find_repeated_letters(s)}")