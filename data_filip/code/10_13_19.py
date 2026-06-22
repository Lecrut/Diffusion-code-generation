import re

def reverse_words(sentence: str) -> str:
    if not sentence:
        return sentence
    pattern = re.compile(r'\s+\S+|\s+')
    tokens = pattern.findall(sentence)
    words = [token for token in tokens if not token.startswith(' ')]
    words.reverse()
    result = []
    word_index = 0
    for token in tokens:
        if token.startswith(' '):
            result.append(token)
        else:
            result.append(words[word_index])
            word_index += 1
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "Hello   world  this  is  a test"
    reversed_output = reverse_words(sample_input)
    print(reversed_output)