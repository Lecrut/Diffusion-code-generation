def capitalize_first_letter(s):
    return ' '.join(word[0].upper() + word[1:] for word in s.split())

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    result = capitalize_first_letter(sample_string)
    print(result)