def capitalize_first_letter(s):
    return ' '.join(word[0].upper() + word[1:] for word in s.split())

if __name__ == '__main__':
    sample_input = "hello world! this is a TEST."
    result = capitalize_first_letter(sample_input)
    print(result)