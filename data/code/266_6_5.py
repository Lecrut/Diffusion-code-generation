def count_words_starting_with(text, letter):
    return sum(1 for word in text.split() if word.startswith(letter))

if __name__ == '__main__':
    sample_text = "apple banana apple orange"
    starting_letter = 'a'
    print(count_words_starting_with(sample_text, starting_letter))