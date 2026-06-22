import re

def find_duplicate_words(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    word_count = {}
    duplicates = []
    
    for token in tokens:
        if token in word_count:
            word_count[token] += 1
        else:
            word_count[token] = 1
    
    for word, count in word_count.items():
        if count > 1:
            duplicates.append(word)
    
    return duplicates

if __name__ == '__main__':
    sample_text = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
    result = find_duplicate_words(sample_text)
    print(result)