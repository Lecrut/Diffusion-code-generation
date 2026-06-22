import re

def reverse_words_preserve_spaces(sentence):
    parts = re.split(r'(\b)', sentence)
    words = [part for part in parts if not part.isspace() and not re.match(r'^\b$', part)]
    words.reverse()
    result = []
    word_index = 0
    for part in parts:
        if re.match(r'^\b$', part):
            result.append(word_index)
            word_index += 1
        elif part.isspace():
            result.append(part)
        else:
            result.append(words[word_index])
            word_index += 1
    reversed_words = []
    word_index = 0
    for i, part in enumerate(parts):
        if re.match(r'^\b$', part):
            reversed_words.append(words[word_index])
            word_index += 1
        else:
            reversed_words.append(part)
    
    final_parts = []
    word_ptr = 0
    for part in parts:
        if re.match(r'^\b$', part):
            final_parts.append(words[word_ptr])
            word_ptr += 1
        else:
            final_parts.append(part)
    
    return ''.join(final_parts)

if __name__ == '__main__':
    sample_input = "Hello  world   this is a  test"
    result = reverse_words_preserve_spaces(sample_input)
    print(result)