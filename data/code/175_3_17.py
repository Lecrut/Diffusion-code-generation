def extract_words(sentence):
    words = [word for word in sentence.split() if word]
    return words

if __name__ == '__main__':
    sample_sentence1 = "Hello, world! This is a test sentence with various spaces and punctuation."
    sample_sentence2 = "  \tWord1, Word2; Word3... "
    sample_sentence3 = "NoPunctuationHere"
    
    result1 = extract_words(sample_sentence1)
    result2 = extract_words(sample_sentence2)
    result3 = extract_words(sample_sentence3)
    
    print(f"Input: '{sample_sentence1}'")
    print(f"Output: {result1}")
    print("-" * 20)
    print(f"Input: '{sample_sentence2}'")
    print(f"Output: {result2}")
    print("-" * 20)
    print(f"Input: '{sample_sentence3}'")
    print(f"Output: {result3}")