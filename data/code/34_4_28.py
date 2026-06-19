def capitalize_first_letter(string):
    return ' '.join(word.capitalize() for word in string.split())

if __name__ == '__main__':
    sample_input = "hello world from alibaba cloud"
    result = capitalize_first_letter(sample_input)
    print(result)