def reverse_words_preserve_spacing(s):
    if not s:
        return s

    chars = list(s)
    n = len(chars)
    left = 0
    right = n - 1

    while left < right:
        if chars[left] == ' ' and chars[right] == ' ':
            left += 1
            right -= 1
        elif chars[left] == ' ':
            left += 1
        elif chars[right] == ' ':
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    result = ''.join(chars)
    words = result.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])

    final_chars = list(result)
    word_index = 0
    i = 0
    while i < len(final_chars):
        if final_chars[i] != ' ':
            j = i
            while j < len(final_chars) and final_chars[j] != ' ':
                j += 1
            new_word = reversed_words[word_index]
            for k in range(len(new_word)):
                final_chars[i + k] = new_word[k]
            word_index += 1
            i = j
        else:
            i += 1

    return ''.join(final_chars)

if __name__ == '__main__':
    print(reverse_words_preserve_spacing("hello world"))
    print(reverse_words_preserve_spacing("  hello   world  "))
    print(reverse_words_preserve_spacing("a"))
    print(reverse_words_preserve_spacing("  "))
    print(reverse_words_preserve_spacing(""))
    print(reverse_words_preserve_spacing("one two three"))