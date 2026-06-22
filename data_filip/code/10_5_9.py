import re

def reverse_words(sentence):
    if not sentence:
        return ""
    pattern = re.compile(r'\S+')
    words = pattern.findall(sentence)
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_input = "  Hello   world   this   is   a   test  "
    result = reverse_words(sample_input)
    print(result)