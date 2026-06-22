import re

def reverse_words(sentence):
    words = re.split(r'\s+', sentence.strip())
    words = [w for w in words if w]
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    result = reverse_words("  Hello   World  ")
    print(result)