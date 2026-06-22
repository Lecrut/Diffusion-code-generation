def words_starting_with(text, letter):
    words = text.lower().split()
    matching_words = [word for word in words if word.startswith(letter)]
    return matching_words

if __name__ == '__main__':
    sample_text = "An apple a day keeps the doctor away"
    starting_letter = 'a'
    result = words_starting_with(sample_text, starting_letter)
    print(result)