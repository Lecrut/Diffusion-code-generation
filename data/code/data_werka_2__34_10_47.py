def capitalize_initials(s):
    return ' '.join(word.capitalize() if word else '' for word in s.split())

if __name__ == '__main__':
    SAMPLE_STRING = "hello world from alibaba cloud"
    capitalized_string = capitalize_initials(SAMPLE_STRING)
    print(capitalized_string)