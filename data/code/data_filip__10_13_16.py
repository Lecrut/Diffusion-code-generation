import re

def reverse_words_preserving_spaces(sentence):
    tokens = re.findall(r'\s+\S+|\s+|\S+', sentence)
    words = [token for token in tokens if not re.match(r'^\s+$', token)]
    words.reverse()
    result = []
    word_index = 0
    for token in tokens:
        if re.match(r'^\s+$', token):
            result.append(token)
        else:
            result.append(words[word_index])
            word_index += 1
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "  Hello   world  this  is  a   test  "
    output = reverse_words_preserving_spaces(sample_input)
    print(output)