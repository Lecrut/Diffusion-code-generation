import re

def reverse_words(sentence):
    tokens = re.findall(r'\S+|\s+', sentence)
    words = [token for token in tokens if not token.isspace()]
    spaces = [token for token in tokens if token.isspace()]
    words.reverse()
    result = []
    word_idx = 0
    space_idx = 0
    while word_idx < len(words) or space_idx < len(spaces):
        if word_idx < len(words):
            result.append(words[word_idx])
            word_idx += 1
        if space_idx < len(spaces):
            result.append(spaces[space_idx])
            space_idx += 1
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "Hello   World\t\t\tTest\n\nCase"
    output = reverse_words(sample_input)
    print(output)