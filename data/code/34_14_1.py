def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())
if __name__ == '__main__':
    test_string = "this is a sample string for testing"
    result = capitalize_words(test_string)
    print(result)