def count_consonants(word):
    consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    if not word:
        return 0
    count = 0
    lower_word = word.lower()
    for char in lower_word:
        if char in consonant_list:
            count += 1
    return count

if __name__ == '__main__':
    test_word = "Programming"
    result = count_consonants(test_word)
    print(result)