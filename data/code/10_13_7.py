import re

def reverse_words_in_sentence(sentence):
    words = re.findall(r'\S+', sentence)
    words.reverse()
    result = re.sub(r'\S+', lambda m: words.pop(0), sentence)
    return result

if __name__ == '__main__':
    sample = "hello   world  foo"
    print(reverse_words_in_sentence(sample))
    sample2 = "  leading  spaces  "
    print(reverse_words_in_sentence(sample2))
    sample3 = "one"
    print(reverse_words_in_sentence(sample3))