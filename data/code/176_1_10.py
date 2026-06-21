def unique_words(text):
    word_list = text.split()
    seen = set()
    result = []
    for word in word_list:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result

if __name__ == '__main__':
    sample_text = "hello world hello Python programming"
    print(unique_words(sample_text))