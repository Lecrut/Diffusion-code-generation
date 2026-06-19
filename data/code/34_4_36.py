def capitalize_first_letter(s):
    return ' '.join(word[0].upper() + word[1:] for word in s.split())

if __name__ == '__main__':
    sample_string = "hello world this is an example string"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)