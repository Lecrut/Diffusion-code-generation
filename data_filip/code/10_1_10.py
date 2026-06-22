def reverse_words_preserve_spaces(sentence):
    if not sentence:
        return sentence

    words = []
    spaces = []

    current_word = []
    current_spaces = []

    i = 0
    n = len(sentence)

    while i < n:
        if sentence[i].isspace():
            current_spaces.append(sentence[i])
            i += 1
        else:
            if current_spaces:
                spaces.append(''.join(current_spaces))
                current_spaces = []
            current_word.append(sentence[i])
            i += 1

    if current_word:
        words.append(''.join(current_word))
    if current_spaces:
        spaces.append(''.join(current_spaces))

    reversed_words = words[::-1]

    result_parts = []
    for idx, word in enumerate(reversed_words):
        result_parts.append(word)
        if idx < len(spaces):
            result_parts.append(spaces[idx])

    return ''.join(result_parts)

if __name__ == '__main__':
    sample1 = "hello   world"
    sample2 = "  spaces  everywhere  "
    sample3 = "one"
    sample4 = "  "
    sample5 = "a  b   c d"

    print(reverse_words_preserve_spaces(sample1))
    print(reverse_words_preserve_spaces(sample2))
    print(reverse_words_preserve_spaces(sample3))
    print(reverse_words_preserve_spaces(sample4))
    print(reverse_words_preserve_spaces(sample5))