import re

def reverse_words(sentence):
    parts = re.split(r'(\s+)', sentence)
    words = [part for part in parts if not part.isspace()]
    reversed_words = words[::-1]
    result_parts = []
    word_idx = 0
    for part in parts:
        if part.isspace():
            result_parts.append(part)
        else:
            result_parts.append(reversed_words[word_idx])
            word_idx += 1
    return ''.join(result_parts)

if __name__ == '__main__':
    sample_input = "  Hello   world!  "
    output = reverse_words(sample_input)
    print(f"'{output}'")