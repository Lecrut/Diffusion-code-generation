import re

def reverse_words(sentence):
    if not sentence:
        return sentence
    tokens = re.findall(r'\S+|\s+', sentence)
    words = [token for token in tokens if not token.isspace()]
    spaces = [token for token in tokens if token.isspace()]
    words.reverse()
    result_parts = []
    word_idx = 0
    space_idx = 0
    is_space_next = len(tokens) > 0 and tokens[0].isspace()
    for _ in range(len(tokens)):
        if is_space_next:
            result_parts.append(spaces[space_idx])
            space_idx += 1
        else:
            result_parts.append(words[word_idx])
            word_idx += 1
        is_space_next = not is_space_next
    return ''.join(result_parts)

if __name__ == '__main__':
    sample_text = "Hello   world\tthis is  a test"
    reversed_result = reverse_words(sample_text)
    print(reversed_result)