def extract_distinct_words(text):
    words = text.split()
    distinct_words = set(words)
    sorted_words = sorted(distinct_words)
    return sorted_words

if __name__ == '__main__':
    sample_text = "hello world hello python programming"
    result = extract_distinct_words(sample_text)
    print(result)