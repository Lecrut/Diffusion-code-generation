import re

def reverse_words_maintain_spaces(sentence):
    if not sentence:
        return sentence
    words = re.findall(r'\S+', sentence)
    reversed_words = words[::-1]
    parts = re.split(r'(\s+)', sentence)
    result = []
    word_index = 0
    for part in parts:
        if part.strip():
            result.append(reversed_words[word_index])
            word_index += 1
        else:
            result.append(part)
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "Hello   world  this is   a  test"
    print(reverse_words_maintain_spaces(sample_input))