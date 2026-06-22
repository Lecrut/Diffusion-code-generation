def find_words_starting_with(text, letter):
    return [word for word in text.split() if word.startswith(letter)]

if __name__ == '__main__':
    sample_text = "apple banana cherry apricot blueberry"
    starting_letter = 'a'
    print(find_words_starting_with(sample_text, starting_letter))