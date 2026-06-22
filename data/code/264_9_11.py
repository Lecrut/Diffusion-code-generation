import re

def group_words_by_initial(text):
    words = re.findall(r'\b\w+\b', text.lower())
    grouped_words = {}
    for word in words:
        initial = word[0]
        if initial not in grouped_words:
            grouped_words[initial] = []
        grouped_words[initial].append(word)
    return grouped_words

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    result = group_words_by_initial(sample_text)
    print(result)