def extract_distinct_words(text):
    word_map = {}
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            word_map[char.lower()] = True
    words = list(word_map.keys())
    return sorted(words)

if __name__ == '__main__':
    sample_text = "Hello world hello Python programming is fun"
    distinct_words = extract_distinct_words(sample_text)
    print(distinct_words)