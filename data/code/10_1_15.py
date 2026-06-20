def reverse_words_preserve_whitespace(sentence):
    if not sentence:
        return sentence
    import re
    words = re.findall('\\S+', sentence)
    separators = re.findall('\\s+', sentence)
    if not words:
        return sentence
    reversed_words = words[::-1]
    result = []
    word_index = 0
    i = 0
    while i < len(sentence):
        if sentence[i].isspace():
            end = i
            while end < len(sentence) and sentence[end].isspace():
                end += 1
            sep = sentence[i:end]
            result.append(sep)
            i = end
        else:
            if word_index < len(reversed_words):
                result.append(reversed_words[word_index])
                word_index += 1
            end = i
            while end < len(sentence) and (not sentence[end].isspace()):
                end += 1
            i = end
    return ''.join(result)
if __name__ == '__main__':
    sample_sentence = 'Hello   World!  This is  a test.'
    result = reverse_words_preserve_whitespace(sample_sentence)
    print(result)