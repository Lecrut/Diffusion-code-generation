def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if len(s) == 0:
        return s
    first_char = ord(s[0])
    if first_char >= ord('a') and first_char <= ord('z'):
        first_char -= (ord('a') - ord('A'))
    return chr(first_char) + s[1:]

if __name__ == '__main__':
    sample_values = ["hello", "WORLD", "python", "", "a"]
    for value in sample_values:
        print(capitalize_first_letter(value))