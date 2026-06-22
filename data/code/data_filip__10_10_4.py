def reverse_words(s):
    words = []
    spaces = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == ' ':
            space_count = 0
            while i < n and s[i] == ' ':
                space_count += 1
                i += 1
            spaces.append(space_count)
        else:
            word = ''
            while i < n and s[i] != ' ':
                word += s[i]
                i += 1
            words.append(word)
    
    if not words:
        return ''.join(' ' * sp for sp in spaces)
    
    reversed_words = words[::-1]
    result = []
    for idx, word in enumerate(reversed_words):
        result.append(word)
        if idx < len(spaces):
            result.append(' ' * spaces[idx])
    
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "Hello   World"
    sample2 = "  leading spaces"
    sample3 = "trailing spaces  "
    sample4 = "   "
    sample5 = ""
    sample6 = "Single"
    sample7 = "One Two Three"
    
    print(reverse_words(sample1))
    print(reverse_words(sample2))
    print(reverse_words(sample3))
    print(reverse_words(sample4))
    print(reverse_words(sample5))
    print(reverse_words(sample6))
    print(reverse_words(sample7))