def group_words_by_initial(text):
    result = {}
    for word in text.split():
        initial = word[0].lower()
        if initial not in result:
            result[initial] = []
        result[initial].append(word)
    return result

if __name__ == '__main__':
    sample_text = "apple banana apple orange banana grape"
    print(group_words_by_initial(sample_text))