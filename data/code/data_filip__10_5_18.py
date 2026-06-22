import re

def reverse_words(sentence):
    words = re.split(r'(\s+)', sentence)
    text_words = [w for w in words if not re.match(r'^\s+$', w)]
    text_words.reverse()
    parts = []
    word_idx = 0
    for part in words:
        if re.match(r'^\s+$', part):
            parts.append(part)
        else:
            parts.append(text_words[word_idx])
            word_idx += 1
    return ''.join(parts)

if __name__ == '__main__':
    sample_sentence = "  Hello   world!  "
    result = reverse_words(sample_sentence)
    print(result)