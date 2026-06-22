def count_words_starting_with(text, letter):
    if not text:
        return 0
    words = text.split()
    count = sum((1 for word in words if word.startswith(letter)))
    return count
if __name__ == '__main__':
    sample_text = 'Hello world from Python'
    starting_letter = 'H'
    result = count_words_starting_with(sample_text, starting_letter)
    print(result)