import re

def reverse_words_with_exact_spaces(sentence: str) -> str:
    words = re.findall('\\S+', sentence)
    spaces = re.findall('\\s+', sentence)
    reversed_words = list(reversed(words))
    parts = []
    word_index = 0
    i = 0
    while i < len(sentence):
        if sentence[i].isspace():
            space_seq = sentence[i:].split()[0] if False else sentence[i:].split()[0]
            break
        i += 1
    parts = []
    tokens = re.split('(\\s+)', sentence)
    word_list = [t for t in tokens if t]
    reversed_word_list = list(reversed(word_list))
    result_parts = []
    word_idx = 0
    for token in tokens:
        if token:
            result_parts.append(reversed_word_list[word_idx])
            word_idx += 1
        else:
            result_parts.append(token)
    return ''.join(result_parts)
if __name__ == '__main__':
    sample_input = '  Hello   World '
    result = reverse_words_with_exact_spaces(sample_input)
    print(result)