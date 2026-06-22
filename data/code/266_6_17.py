def count_words_starting_with(text, letter):
    if not text or not letter:
        return 0
    words = text.split()
    count = sum((1 for word in words if word.startswith(letter)))
    return count
if __name__ == '__main__':
    sample_text = 'The quick brown fox jumps over the lazy dog'
    letter_to_check = 'o'
    result = count_words_starting_with(sample_text, letter_to_check)
    print(result)