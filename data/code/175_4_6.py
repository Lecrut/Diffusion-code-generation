import re

def extract_words(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', sentence)
    return words

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence for testing purposes"
    extracted_words = extract_words(sample_sentence)
    print(extracted_words)