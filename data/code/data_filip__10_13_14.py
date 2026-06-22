import re

def reverse_words_in_sentence(sentence):
    tokens = re.split(r'(\s+)', sentence)
    words = [token for token in tokens if token.strip()]
    words.reverse()
    result = []
    word_index = 0
    for token in tokens:
        if token.strip():
            result.append(words[word_index])
            word_index += 1
        else:
            result.append(token)
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "Hello   World"
    sample2 = "  Python  is   awesome  "
    sample3 = "One"
    sample4 = "   "
    sample5 = ""
    print(reverse_words_in_sentence(sample1))
    print(reverse_words_in_sentence(sample2))
    print(reverse_words_in_sentence(sample3))
    print(reverse_words_in_sentence(sample4))
    print(reverse_words_in_sentence(sample5))