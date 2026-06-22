def reverse_words(sentence):
    if not sentence:
        return ""
    chars = list(sentence)
    n = len(chars)
    
    def reverse_in_place(start, end):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
    
    reverse_in_place(0, n - 1)
    
    start = 0
    for end in range(n):
        if chars[end] == ' ':
            reverse_in_place(start, end - 1)
            start = end + 1
    
    reverse_in_place(start, n - 1)
    
    return ''.join(chars)

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "Python is awesome",
        "Reverse these words",
        "A",
        "  Leading spaces",
        "Trailing spaces  ",
        "Multiple   spaces   between",
        "",
        "SingleWord",
        "Two Words"
    ]
    for s in sample_sentences:
        print(repr(reverse_words(s)))