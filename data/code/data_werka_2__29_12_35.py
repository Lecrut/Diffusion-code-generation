def reverse_word(word):
    reversed_chars = []
    for i in range(len(word) - 1, -1, -1):
        reversed_chars.append(word[i])
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "world"
    print(reverse_word(sample_word))