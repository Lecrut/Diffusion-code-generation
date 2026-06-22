def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    SAMPLE_STRING = "capitalize each word in this sentence"
    capitalized_string = capitalize_words(SAMPLE_STRING)
    print(capitalized_string)