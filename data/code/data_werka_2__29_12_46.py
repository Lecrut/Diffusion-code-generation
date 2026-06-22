def reverse_word(word):
    START_INDEX = 0
    END_INDEX = len(word) - 1
    
    def reverse_recursive(start, end, chars):
        if start > end:
            return ''.join(chars)
        chars[start], chars[end] = chars[end], chars[start]
        return reverse_recursive(start + 1, end - 1, chars)
    
    char_list = list(word)
    return reverse_recursive(START_INDEX, END_INDEX, char_list)

if __name__ == '__main__':
    sample_word = "alibaba"
    print(reverse_word(sample_word))