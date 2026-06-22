def capitalize_first_letter_only(s):
    return ' '.join(word[0].upper() + word[1:] for word in s.split())

if __name__ == '__main__':
    sample_input = "hello world from alibaba cloud"
    result = capitalize_first_letter_only(sample_input)
    print(result)