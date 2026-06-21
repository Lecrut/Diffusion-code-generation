def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])

if __name__ == '__main__':
    sample_sentence1 = "Hello world this is a test"
    result1 = reverse_words(sample_sentence1)
    print(f"Original: {sample_sentence1}")
    print(f"Reversed: {result1}")
    
    sample_sentence2 = "Optimization is key"
    result2 = reverse_words(sample_sentence2)
    print(f"Original: {sample_sentence2}")
    print(f"Reversed: {result2}")
    
    sample_sentence3 = "a single word"
    result3 = reverse_words(sample_sentence3)
    print(f"Original: {sample_sentence3}")
    print(f"Reversed: {result3}")