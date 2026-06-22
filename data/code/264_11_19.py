import re

def extract_words(sentences):
    if not isinstance(sentences, list) or not all(isinstance(sentence, str) for sentence in sentences):
        raise ValueError("Input must be a list of strings.")
    
    words = set()
    pattern = r'\b\w+\b'
    for sentence in sentences:
        found_words = re.findall(pattern, sentence)
        words.update(found_words)
    
    return sorted(words)

if __name__ == '__main__':
    sample_sentences1 = ["Hello world! This is a test sentence with numbers 123 and symbols @#."]
    sample_sentences2 = ["  Multiple   spaces\tand\nnewlines are handled correctly. Word test again."]
    sample_sentences3 = ["Alpha beta gamma alpha"]
    
    result1 = extract_words(sample_sentences1)
    print(f"Result for sample_sentences1: {result1}")
    
    result2 = extract_words(sample_sentences2)
    print(f"Result for sample_sentences2: {result2}")
    
    result3 = extract_words(sample_sentences3)
    print(f"Result for sample_sentences3: {result3}")