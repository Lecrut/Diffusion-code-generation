def reverse_words_preserve_spacing(s: str) -> str:
    if not s:
        return ""

    words = s.split()
    if not words:
        return s

    reversed_words = words[::-1]
    n = len(s)
    result = [''] * n

    word_idx = 0
    i = 0
    while i < n:
        if s[i] == ' ':
            result[i] = ' '
            i += 1
        else:
            j = i
            while j < n and s[j] != ' ':
                j += 1
            word = reversed_words[word_idx]
            word_idx += 1
            for k in range(len(word)):
                result[i + k] = word[k]
            i = j

    return ''.join(result)

if __name__ == '__main__':
    print(reverse_words_preserve_spacing("  hello   world  "))
    print(reverse_words_preserve_spacing("Python is awesome"))
    print(reverse_words_preserve_spacing("a"))
    print(reverse_words_preserve_spacing(""))
    print(reverse_words_preserve_spacing("  "))