def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_strings = ["hello", "world", "", "a"]
    for s in sample_strings:
        result = capitalize_first(s)
        print(result)