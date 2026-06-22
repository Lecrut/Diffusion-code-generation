def first_letters_of_words(input_string):
    words = input_string.split()
    result = ''.join((word[0] for word in words))
    return result
if __name__ == '__main__':
    sample_input = '  This   is  a   test string with various   whitespace.  '
    output = first_letters_of_words(sample_input)
    print(output)