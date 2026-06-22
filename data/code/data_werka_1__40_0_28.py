def first_letter_of_each_word(input_string):
    words = input_string.split()
    first_letters = [word[0] for word in words]
    return ''.join(first_letters)
if __name__ == '__main__':
    sample_input = '  This   is  a   test string.  '
    result = first_letter_of_each_word(sample_input)
    print(result)