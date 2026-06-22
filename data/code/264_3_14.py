import re

def extract_words(text):
    return re.findall(r'\b\w+\b', text.lower())

def filter_words(words):
    return [word for word in words if len(word) >= 3]

def find_duplicates(words):
    word_count = {}
    duplicates = set()
    
    for word in words:
        if word in word_count:
            duplicates.add(word)
        else:
            word_count[word] = 1
    
    return list(duplicates)

def process_text(text):
    words = extract_words(text)
    filtered_words = filter_words(words)
    return find_duplicates(filtered_words)

if __name__ == '__main__':
    sample_text = "This is a large block of text that needs to be processed efficiently. Short words like 'a', 'is', and 'of' should be removed. Performance matters greatly."
    result = process_text(sample_text)
    print(result)