def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    samples = ["hello", "world", "a", "", "python"]
    for sample in samples:
        print(capitalize_first(sample))