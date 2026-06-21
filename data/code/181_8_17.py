def filter_words_with_vowels(words):
    vowels = 'aeiouAEIOU'
    result = []
    for word in words:
        if word and any((char in vowels for char in word)):
            result.append(word)
    return result
if __name__ == '__main__':
    sample_text = ['hello', 'world', '', 'rhythm', 'bcdfghjklmn']
    filtered_words = filter_words_with_vowels(sample_text)
    print(filtered_words)