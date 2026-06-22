def find_words_starting_with(text, letter):
    words = text.lower().split()
    result = [word for word in words if word.startswith(letter)]
    return result

if __name__ == '__main__':
    sample_text = "This is a sample sentence for finding words starting with the letter 't'"
    result = find_words_starting_with(sample_text, 't')
    print(result)