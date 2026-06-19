def first_letter_of_each_word(input_string):
    words = input_string.split()
    result = ''.join((word[0] for word in words if word))
    return result
if __name__ == '__main__':
    sample_input1 = 'Hello   world'
    sample_input2 = '  This is a test  '
    sample_input3 = 'Python\tis\tawesome'
    print(first_letter_of_each_word(sample_input1))
    print(first_letter_of_each_word(sample_input2))
    print(first_letter_of_each_word(sample_input3))