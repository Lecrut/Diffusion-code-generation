import re

def reverse_words(sentence: str) -> str:
    words = re.split(r'(\s+)', sentence)
    text_parts = [w for w in words if w and not re.match(r'\s', w)]
    text_parts.reverse()
    result = []
    word_idx = 0
    for part in words:
        if re.match(r'\s', part):
            result.append(part)
        else:
            result.append(text_parts[word_idx])
            word_idx += 1
    return ''.join(result)

if __name__ == '__main__':
    sentence = "  Hello   world!  This   is  Python.  "
    result = reverse_words(sentence)
    print(result)