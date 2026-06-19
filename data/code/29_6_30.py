def reverse_word(word):
    return word[::-1]

if __name__ == '__main__':
    SAMPLE_WORD = "Alibaba"
    REVERSED_WORD = reverse_word(SAMPLE_WORD)
    print(REVERSED_WORD)