def count_words(words_list):
    if not words_list:
        return 0
    word_count = sum(1 for item in words_list if item.strip())
    return word_count

if __name__ == '__main__':
    sample_texts = [
        "This is a sample sentence for testing the word counter.",
        "Another test case with different spacing and punctuation.",
        "",
        "Word one. Word two! Three.",
        "   leading and trailing spaces test   "
    ]
    
    for text in sample_texts:
        print(f"Text: '{text}'")
        print(f"Word count: {count_words(text.split())}")
        print("-" * 20)