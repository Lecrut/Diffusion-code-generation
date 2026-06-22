def reverse_words_preserve_spacing(s):
    if not s:
        return s

    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        if chars[left] == ' ':
            left += 1
        elif chars[right] == ' ':
            right -= 1
        else:
            temp_left = left
            temp_right = right

            while temp_left < temp_right:
                chars[temp_left], chars[temp_right] = chars[temp_right], chars[temp_left]
                temp_left += 1
                temp_right -= 1

            left = temp_left
            right = temp_right

    return ''.join(chars)

if __name__ == '__main__':
    sample1 = "Hello   World"
    sample2 = "  foo  bar  baz "
    sample3 = "SingleWord"
    sample4 = "  "
    sample5 = "a b c"

    print(reverse_words_preserve_spacing(sample1))
    print(reverse_words_preserve_spacing(sample2))
    print(reverse_words_preserve_spacing(sample3))
    print(reverse_words_preserve_spacing(sample4))
    print(reverse_words_preserve_spacing(sample5))