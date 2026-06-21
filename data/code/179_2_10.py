def reverse_sentence(sentence: str) -> str:
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    words = sentence.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_sentence1 = "Hello world this is a test"
    print(f"Original: {sample_sentence1}")
    print(f"Reversed: {reverse_sentence(sample_sentence1)}")
    
    sample_sentence2 = "Optimization is key"
    print(f"Original: {sample_sentence2}")
    print(f"Reversed: {reverse_sentence(sample_sentence2)}")
    
    sample_sentence3 = "a single word"
    print(f"Original: {sample_sentence3}")
    print(f"Reversed: {reverse_sentence(sample_sentence3)}")