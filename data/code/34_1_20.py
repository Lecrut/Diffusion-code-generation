def capitalize_first_letter_only(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    result = capitalize_first_letter_only(sample_input)
    print(result)