def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if len(s) == 0:
        return s
    return s.capitalize()

if __name__ == '__main__':
    sample_values = ["hello", "WORLD", "Python", "", "a"]
    for value in sample_values:
        print(capitalize_first_letter(value))