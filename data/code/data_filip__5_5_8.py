def capitalize_first_char(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_data = "hello world"
    result = capitalize_first_char(sample_data)
    print(result)