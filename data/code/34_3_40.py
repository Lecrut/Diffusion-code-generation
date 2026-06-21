def capitalize_first_letter(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "this is a sample string"
    result = capitalize_first_letter(sample_string)
    print(result)