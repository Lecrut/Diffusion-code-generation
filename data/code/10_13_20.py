import re

def reverse_words(sentence):
    parts = re.split(r'(\s+)', sentence)
    words = [p for p in parts if not re.match(r'\s', p)]
    reversed_words = words[::-1]
    result_parts = []
    word_idx = 0
    for p in parts:
        if re.match(r'\s', p):
            result_parts.append(p)
        else:
            result_parts.append(reversed_words[word_idx])
            word_idx += 1
    return ''.join(result_parts)

if __name__ == '__main__':
    sentence = "Hello   World  Python"
    result = reverse_words(sentence)
    print(result)