import re

def reverse_words(sentence):
    if not sentence:
        return ""
    words = re.findall(r'\S+', sentence)
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_input = "Hello   world\tthis is\na test"
    result = reverse_words(sample_input)
    print(result)