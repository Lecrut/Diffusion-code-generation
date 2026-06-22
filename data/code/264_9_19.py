def categorize_words(text):
    word_dict = {}
    words = text.split()
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in word_dict:
            word_dict[first_letter] = []
        word_dict[first_letter].append(word)
    return word_dict

if __name__ == '__main__':
    sample_text = "apple banana apple orange banana cherry"
    result = categorize_words(sample_text)
    print(result)