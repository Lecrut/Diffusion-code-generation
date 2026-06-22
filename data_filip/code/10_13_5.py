import re

def reverse_words_in_sentence(s):
    tokens = re.split(r'(\s+)', s)
    words = [token for token in tokens if token.strip()]
    spaces = [token for token in tokens if not token.strip() or token == '']
    result = []
    word_iter = reversed(words)
    space_iter = iter(spaces)
    for token in tokens:
        if token.strip():
            result.append(next(word_iter))
        else:
            result.append(token)
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "hello   world"
    sample2 = "  leading spaces"
    sample3 = "trailing spaces   "
    sample4 = "single"
    sample5 = "  multiple   spaces   here  "
    print(reverse_words_in_sentence(sample1))
    print(reverse_words_in_sentence(sample2))
    print(reverse_words_in_sentence(sample3))
    print(reverse_words_in_sentence(sample4))
    print(reverse_words_in_sentence(sample5))