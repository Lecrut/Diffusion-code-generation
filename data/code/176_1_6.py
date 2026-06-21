def unique_words(text):
    word_set = set()
    result = []
    for word in text.split():
        if word not in word_set:
            word_set.add(word)
            result.append(word)
    return result

if __name__ == '__main__':
    sample_text = "hello world hello Python world"
    print(unique_words(sample_text))