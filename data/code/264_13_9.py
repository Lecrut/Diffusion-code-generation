def most_frequent_word(text):
    if not isinstance(text, str) or not text:
        raise ValueError("Input must be a non-empty string")
    
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    most_frequent = max(word_count.items(), key=lambda x: x[1])
    return most_frequent

if __name__ == '__main__':
    sample_text = "hello world hello python programming is fun and exciting"
    try:
        result = most_frequent_word(sample_text)
        print(f"The most frequent word is '{result[0]}' with a count of {result[1]}")
    except ValueError as e:
        print(e)