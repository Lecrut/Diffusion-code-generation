def capitalize_first(s):
    if not s:
        return s
    return chr(ord(s[0]).lower() if s[0].islower() else ord(s[0])) + s[1:]

if __name__ == '__main__':
    sample_strings = ["hello", "world", "", "a", "Z"]
    for word in sample_strings:
        result = capitalize_first(word)
        print(result)