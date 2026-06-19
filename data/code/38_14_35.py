def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def find_repeated_characters(s):
    validate_input(s)
    from collections import Counter
    char_count = Counter(s)
    repeated_chars = [char for char, count in char_count.items() if count > 1]
    return sorted(repeated_chars)

if __name__ == '__main__':
    sample_string = "example string with some repeated characters"
    result = find_repeated_characters(sample_string)
    print(result)