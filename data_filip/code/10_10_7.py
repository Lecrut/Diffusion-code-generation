def reverse_words_preserve_spacing(s: str) -> str:
    if not s:
        return s

    words = []
    left = 0
    n = len(s)
    while left < n:
        while left < n and s[left] == ' ':
            left += 1
        if left == n:
            break
        right = left
        while right < n and s[right] != ' ':
            right += 1
        words.append(s[left:right])
        left = right

    words.reverse()

    result = []
    word_idx = 0
    left = 0
    while left < n:
        if s[left] == ' ':
            result.append(' ')
            left += 1
        else:
            result.append(words[word_idx])
            word_idx += 1
            while left < n and s[left] != ' ':
                left += 1

    return ''.join(result)

if __name__ == '__main__':
    print(reverse_words_preserve_spacing('hello world'))
    print(reverse_words_preserve_spacing('  hello   world  '))
    print(reverse_words_preserve_spacing('a'))
    print(reverse_words_preserve_spacing('  '))
    print(reverse_words_preserve_spacing(''))
    print(reverse_words_preserve_spacing('foo   bar baz'))
    print(reverse_words_preserve_spacing('one two'))