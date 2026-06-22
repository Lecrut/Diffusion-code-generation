def capitalize_first_letter(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_input = "hello world from alibaba cloud"
    result = capitalize_first_letter(sample_input)
    print(result)