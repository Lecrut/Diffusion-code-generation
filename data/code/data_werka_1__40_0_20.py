def first_letters_of_words(input_string):
    import re
    words = re.split(r'\s+', input_string.strip())
    return ''.join(word[0] for word in words if word)

if __name__ == '__main__':
    sample_input = "  This   is  a   test string with  irregular spacing.  "
    result = first_letters_of_words(sample_input)
    print(result)