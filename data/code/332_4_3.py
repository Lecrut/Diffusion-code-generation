def count_total_vowels(*words):
    total_vowels = 0
    vowels = "aeiouAEIOU"
    for word in words:
        for char in word:
            if char in vowels:
                total_vowels += 1
    return total_vowels
if __name__ == '__main__':
    word1 = "hello"
    word2 = "world"
    word3 = ""
    word4 = "programming"
    result = count_total_vowels(word1, word2, word3, word4)
    print(result)