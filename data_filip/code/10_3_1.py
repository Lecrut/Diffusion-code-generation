def reverse_words_in_sentence(sentence):
    if not sentence:
        return sentence
    chars = list(sentence)
    n = len(chars)
    start = 0
    while start < n:
        while start < n and chars[start] == ' ':
            start += 1
        if start == n:
            break
        end = start + 1
        while end < n and chars[end] != ' ':
            end += 1
        left, right = start, end - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        start = end
    return ''.join(chars)

if __name__ == '__main__':
    sample = "Hello World from Python"
    print(reverse_words_in_sentence(sample))