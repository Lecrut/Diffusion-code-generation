def capitalize_first(s):
    return s[0].upper() + s[1:] if s else ''

if __name__ == '__main__':
    sample_string = "hello world"
    capitalized_string = capitalize_first(sample_string)
    print(capitalized_string)