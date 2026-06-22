import re

def reverse_words_preserving_spaces(sentence):
    if not sentence:
        return sentence
    pattern = re.compile(r'(\S+)|(\s+)')
    tokens = pattern.findall(sentence)
    words = []
    for match in tokens:
        if match[0]:
            words.append(match[0])
    words.reverse()
    result = []
    word_index = 0
    for match in tokens:
        if match[0]:
            result.append(words[word_index])
            word_index += 1
        else:
            result.append(match[1])
    return "".join(result)

if __name__ == '__main__':
    sample_input = "Hello   world  this is  a  test"
    output = reverse_words_preserving_spaces(sample_input)
    print(output)