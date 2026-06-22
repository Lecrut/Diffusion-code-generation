def reverse_words_preserve_whitespace(sentence: str) -> str:
    if not sentence:
        return ''
    words = sentence.split()
    reversed_words = list(reversed(words))
    import re
    whitespace_chunks = re.split('(\\S+)', sentence)
    result = []
    word_index = 0
    for chunk in whitespace_chunks:
        if chunk.strip() == '':
            result.append(chunk)
        elif word_index < len(reversed_words):
            result.append(reversed_words[word_index])
            word_index += 1
    return ''.join(result)
if __name__ == '__main__':
    input_sentence = 'Hello   World'
    output_sentence = reverse_words_preserve_whitespace(input_sentence)
    print(output_sentence)