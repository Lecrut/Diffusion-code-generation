def count_words(text):
    if not text:
        return 0
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_texts = [
        "This is a sample sentence for testing the word counter.",
        "Another test case with different spacing and punctuation.",
        "",
        "Word one. Word two! Three."
    ]
    
    for text in sample_texts:
        print(f"Text: '{text}'")
        print(f"Word count: {count_words(text)}")
        print("-" * 20)