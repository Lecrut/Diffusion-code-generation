def words_starting_with(text, letter):
    return [word for word in text.split() if word.lower().startswith(letter)]

if __name__ == '__main__':
    sample_text = "This is a sample sentence starting with specific letters. This starts with T."
    result = words_starting_with(sample_text, 't')
    print(result)