import re

def reverse_words_preserve_spaces(sentence):
    if not sentence:
        return sentence
    pattern = r'\S+|\s+'
    tokens = re.findall(pattern, sentence)
    words = [token for token in tokens if not token.isspace()]
    reversed_words = list(reversed(words))
    result_tokens = []
    word_index = 0
    for token in tokens:
        if token.isspace():
            result_tokens.append(token)
        else:
            result_tokens.append(reversed_words[word_index])
            word_index += 1
    return ''.join(result_tokens)

if __name__ == '__main__':
    sample_input = "Hello   world  this is   a test"
    output = reverse_words_preserve_spaces(sample_input)
    print(output)