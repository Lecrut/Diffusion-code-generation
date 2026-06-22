def capitalize_first_letter(input_string):
    words = input_string.split()
    capitalized_words = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    result = capitalize_first_letter(sample_input)
    print(result)