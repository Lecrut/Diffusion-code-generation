def capitalize_first_letter(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_string = "hello world this is a test string"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)