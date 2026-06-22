def count_words_starting_with(text, letter):
    if not text:
        return 0
    words = text.split()
    valid_letter = letter.lower()
    count = sum((1 for word in words if word.lower().startswith(valid_letter)))
    return count
if __name__ == '__main__':
    sample_text = 'Hello world hello universe'
    sample_letter = 'h'
    print(count_words_starting_with(sample_text, sample_letter))