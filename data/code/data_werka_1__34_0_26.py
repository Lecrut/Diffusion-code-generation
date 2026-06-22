def capitalize_first_letter(s):
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in s.split())

if __name__ == '__main__':
    sample_string = "hello world! this is a TEST string."
    result = capitalize_first_letter(sample_string)
    print(result)