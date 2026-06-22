def capitalize_first_letter(s):
    return s[:1].upper() + s[1:]

if __name__ == '__main__':
    sample_string = "hello world"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)