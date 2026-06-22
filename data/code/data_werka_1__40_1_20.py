def get_first_letters(s):
    return [word[0] for word in s.split() if word]

if __name__ == '__main__':
    sample_string = "Hello world this is a test"
    print(get_first_letters(sample_string))