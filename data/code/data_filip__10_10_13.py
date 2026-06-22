def reverse_words_preserve_spacing(s):
    if not s:
        return s
    chars = list(s)
    n = len(chars)
    chars.reverse()
    i = 0
    while i < n:
        if chars[i] != ' ':
            j = i
            while j < n and chars[j] != ' ':
                j += 1
            left = i
            right = j - 1
            while left < right:
                chars[left], chars[right] = (chars[right], chars[left])
                left += 1
                right -= 1
            i = j
        else:
            i += 1
    return ''.join(chars)
if __name__ == '__main__':
    test_cases = ['Hello   World', '  Hello  World  ', 'Single', '', '   ', 'One Two Three', 'A  B   C     D']
    for test in test_cases:
        result = reverse_words_preserve_spacing(test)
        print(repr(result))