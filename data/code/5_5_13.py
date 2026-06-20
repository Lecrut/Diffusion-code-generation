def capitalize_first(s):
    if not s:
        return s
    return s[:1].upper() + s[1:]

if __name__ == '__main__':
    sample_data = "hello world"
    print(capitalize_first(sample_data))