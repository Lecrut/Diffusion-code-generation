def reverse_words_preserving_spacing(s):
    if not s:
        return s
    chars = list(s)
    n = len(chars)
    i = 0
    words = []
    while i < n:
        if chars[i] != ' ':
            j = i
            while j < n and chars[j] != ' ':
                j += 1
            words.append(''.join(chars[i:j]))
            i = j
        else:
            i += 1
    if not words:
        return s
    reversed_words = words[::-1]
    result = []
    word_idx = 0
    i = 0
    while i < n:
        if chars[i] != ' ':
            j = i
            while j < n and chars[j] != ' ':
                j += 1
            result.append(reversed_words[word_idx])
            word_idx += 1
            i = j
        else:
            result.append(chars[i])
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "the sky is blue"
    sample2 = "  hello world  "
    sample3 = "a   b"
    sample4 = ""
    sample5 = "   "
    print(reverse_words_preserving_spacing(sample1))
    print(reverse_words_preserving_spacing(sample2))
    print(reverse_words_preserving_spacing(sample3))
    print(reverse_words_preserving_spacing(sample4))
    print(reverse_words_preserving_spacing(sample5))