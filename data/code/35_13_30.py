def count_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_word = "AlibabaCloud"
    print(count_vowels(sample_word))