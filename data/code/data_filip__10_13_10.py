import re

def reverse_words_preserve_spaces(sentence):
    if not sentence:
        return sentence
    
    tokens = re.split(r'(\s+)', sentence)
    words = [token for token in tokens if token and not token.isspace()]
    
    reversed_words = words[::-1]
    
    result = []
    word_index = 0
    for token in tokens:
        if token and not token.isspace():
            result.append(reversed_words[word_index])
            word_index += 1
        else:
            result.append(token)
    
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "hello   world"
    sample2 = "  foo bar  baz  "
    sample3 = "one"
    sample4 = ""
    sample5 = "a  b c"
    
    print(reverse_words_preserve_spaces(sample1))
    print(reverse_words_preserve_spaces(sample2))
    print(reverse_words_preserve_spaces(sample3))
    print(reverse_words_preserve_spaces(sample4))
    print(reverse_words_preserve_spaces(sample5))