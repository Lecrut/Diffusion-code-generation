import unicodedata

def contains_normalized_word(text, word):
    normalized_text = unicodedata.normalize('NFC', text)
    return word in normalized_text

if __name__ == '__main__':
    sample_text = "Hello, 世界!"
    search_word = "世"
    result = contains_normalized_word(sample_text, search_word)
    print(result)