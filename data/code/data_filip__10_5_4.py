import re

def reverse_words_in_sentence(sentence):
    tokens = re.split(r'(\s+)', sentence)
    words = [token for token in tokens if not re.match(r'^\s+$', token) and token != '']
    reversed_words = words[::-1]
    result = []
    word_iter = iter(reversed_words)
    for token in tokens:
        if re.match(r'^\s+$', token) or token == '':
            result.append(token)
        else:
            try:
                result.append(next(word_iter))
            except StopIteration:
                break
    return ''.join(result)

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "  spaces  around  ",
        "one\ttwo\nthree",
        "No change needed",
        "   leading and   trailing   "
    ]
    for s in sample_sentences:
        print(reverse_words_in_sentence(s))