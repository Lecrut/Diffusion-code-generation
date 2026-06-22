def count_words_starting_with(text, letter):
    if not text:
        return 0
    words = text.split()
    count = sum((1 for word in words if word.lower().startswith(letter.lower())))
    return count
if __name__ == '__main__':
    sample_text = 'Apple banana cherry apricot'
    letter_to_count = 'a'
    result = count_words_starting_with(sample_text, letter_to_count)
    print(result)