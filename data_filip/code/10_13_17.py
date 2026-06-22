import re

def reverse_words_preserve_spaces(sentence: str) -> str:
    words = re.findall('\\S+', sentence)
    spaces = re.findall('\\s+', sentence)
    words.reverse()
    if not words:
        return sentence
    result_parts = []
    word_idx = 0
    space_idx = 0
    tokens = re.findall('\\S+|\\s+', sentence)
    word_count = len(words)
    current_word_idx = 0
    new_tokens = []
    for token in tokens:
        if token.strip():
            new_tokens.append(words[current_word_idx])
            current_word_idx += 1
        else:
            new_tokens.append(token)
    return ''.join(new_tokens)
if __name__ == '__main__':
    input_str = '  Hello   world!  '
    output_str = reverse_words_preserve_spaces(input_str)
    print(output_str)