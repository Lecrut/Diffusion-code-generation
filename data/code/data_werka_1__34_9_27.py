def capitalize_first_letter_only(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_string = "hello world from alibaba cloud"
    result = capitalize_first_letter_only(sample_string)
    print(result)