def capitalize_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    SAMPLE_STRING = "hello world from alibaba cloud"
    capitalized_string = capitalize_each_word(SAMPLE_STRING)
    print(capitalized_string)