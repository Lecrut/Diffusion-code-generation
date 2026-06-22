def find_words_starting_with(text, letter):
    words = text.lower().split()
    matching_words = [word for word in words if word.startswith(letter)]
    return matching_words

if __name__ == '__main__':
    sample_text = "This is a sample sentence with some starting words"
    result = find_words_starting_with(sample_text, 's')
    print(result)