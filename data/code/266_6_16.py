def count_words_starting_with(text, letter):
    if not text:
        return 0
    words = text.split()
    count = 0
    for word in words:
        if word and word[0].lower() == letter.lower():
            count += 1
    return count
if __name__ == '__main__':
    sample_text = 'The quick brown fox jumps over the lazy dog'
    letter_to_count = 'o'
    result = count_words_starting_with(sample_text, letter_to_count)
    print(result)