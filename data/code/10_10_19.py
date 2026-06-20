def reverse_words_preserving_spaces(s):
    chars = list(s)
    n = len(chars)
    left = 0
    while left < n:
        if chars[left] == ' ':
            left += 1
            continue
        right = left
        while right < n and chars[right] != ' ':
            right += 1
        word_end = right - 1
        stack = []
        while left <= word_end:
            stack.append(chars[left])
            left += 1
        left_idx = word_end
        while stack:
            chars[left_idx] = stack.pop()
            left_idx -= 1
    words = []
    current_word = []
    for char in chars:
        if char == ' ':
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        words.append(''.join(current_word))
    words.reverse()
    result = []
    word_index = 0
    i = 0
    while i < n:
        if chars[i] == ' ':
            space_count = 0
            while i < n and chars[i] == ' ':
                space_count += 1
                i += 1
            result.append(' ' * space_count)
        else:
            if word_index < len(words):
                result.append(words[word_index])
                word_index += 1
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "Hello   world  this is   a test"
    result = reverse_words_preserving_spaces(sample_input)
    print(result)