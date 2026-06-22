def capitalize_first_letter(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    SAMPLE_STRING = "this is another test string"
    result = capitalize_first_letter(SAMPLE_STRING)
    print(result)