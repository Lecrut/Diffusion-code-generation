def count_consonants(word):
    vowels = set('aeiouAEIOU')
    return len([char for char in word if char.isalpha() and char not in vowels])

if __name__ == '__main__':
    test_word = "Hello, World! 123"
    result = count_consonants(test_word)
    print(result)
    test_word_2 = "Python3"
    result_2 = count_consonants(test_word_2)
    print(result_2)
    test_word_3 = "AEIOU"
    result_3 = count_consonants(test_word_3)
    print(result_3)
    test_word_4 = "bcdfg"
    result_4 = count_consonants(test_word_4)
    print(result_4)