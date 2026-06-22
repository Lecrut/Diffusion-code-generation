def reverse_words_with_spacing(s):
    if not s:
        return s

    chars = list(s)
    n = len(chars)
    words = []
    i = 0

    while i < n:
        if chars[i] != ' ':
            j = i
            while j < n and chars[j] != ' ':
                j += 1
            words.append(chars[i:j])
            i = j
        else:
            i += 1

    if not words:
        return s

    left = 0
    right = len(words) - 1

    while left < right:
        w1 = words[left]
        w2 = words[right]
        words[left] = w2
        words[right] = w1
        left += 1
        right -= 1

    result_chars = []
    word_idx = 0
    i = 0
    while i < n:
        if chars[i] != ' ':
            j = i
            while j < n and chars[j] != ' ':
                j += 1
            result_chars.extend(words[word_idx])
            word_idx += 1
            i = j
        else:
            result_chars.append(chars[i])
            i += 1

    return ''.join(result_chars)

if __name__ == '__main__':
    samples = [
        "Hello   World",
        "  spaces  everywhere  ",
        "Single",
        "",
        "a   b   c",
        "  ",
        "Leading  ",
        "  Trailing"
    ]
    for sample in samples:
        print(reverse_words_with_spacing(sample))