def capitalize_first_letter_of_each_word(input_string):
    words = input_string.split()
    capitalized_words = []
    for word in words:
        if word:
            capitalized_words.append(word[0].upper() + word[1:])
        else:
            capitalized_words.append('')
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "yet another example with different casing."
    result = capitalize_first_letter_of_each_word(sample_input)
    print(result)