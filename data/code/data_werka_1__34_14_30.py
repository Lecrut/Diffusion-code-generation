def capitalize_first(s):
    return s[:1].upper() + s[1:]

if __name__ == '__main__':
    sample_string = "hello world"
    result = capitalize_first(sample_string)
    print(result)