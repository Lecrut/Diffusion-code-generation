import re

def reverse_words_keep_spaces(sentence: str) -> str:
    pattern = re.compile(r'\b\w+\b')
    words = pattern.findall(sentence)
    reversed_words = list(reversed(words))
    result = []
    word_index = 0
    for match in pattern.finditer(sentence):
        start = match.start()
        end = match.end()
        if start > 0:
            prefix = sentence[match.start():match.start()]
        else:
            prefix = ""
        result.append(reversed_words[word_index])
        word_index += 1
    final_result = ""
    current_pos = 0
    word_idx = 0
    for match in pattern.finditer(sentence):
        final_result += sentence[current_pos:match.start()]
        final_result += reversed_words[word_idx]
        current_pos = match.end()
        word_idx += 1
    final_result += sentence[current_pos:]
    return final_result

if __name__ == '__main__':
    sample_text = "Hello   world  this is   a test"
    print(reverse_words_keep_spaces(sample_text))