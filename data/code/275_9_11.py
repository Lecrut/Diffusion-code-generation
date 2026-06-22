def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

if __name__ == '__main__':
    sample_string = "Python programming is fun!"
    validate_input(sample_string)
    result = count_characters(sample_string)
    print(result)