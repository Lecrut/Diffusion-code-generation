def count_words_starting_with_letter(text, letter):
    words = text.split()
    count = 0
    for word in words:
        if word and word[0].lower() == letter.lower():
            count += 1
    return count
if __name__ == '__main__':
    sample_text = 'Apple banana apple orange Banana'
    target_letter = 'a'
    result = count_words_starting_with_letter(sample_text, target_letter)
    print(result)