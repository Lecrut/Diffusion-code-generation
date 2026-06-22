def group_words_by_initial(text):
    words = text.split()
    grouped_words = {}
    for word in words:
        initial = word[0].lower()
        if initial not in grouped_words:
            grouped_words[initial] = []
        grouped_words[initial].append(word)
    return grouped_words

if __name__ == '__main__':
    sample_text = "apple banana apple orange banana grape"
    result = group_words_by_initial(sample_text)
    print(result)