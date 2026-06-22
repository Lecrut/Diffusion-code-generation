def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    samples = ["hello", "WORLD", "PyThOn", "a", "", "123abc", "ABCdefGHI"]
    for sample in samples:
        print(capitalize_first(sample))