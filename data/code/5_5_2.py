def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_strings = ["hello", "world", "", "a"]
    for sample in sample_strings:
        print(capitalize_first(sample))