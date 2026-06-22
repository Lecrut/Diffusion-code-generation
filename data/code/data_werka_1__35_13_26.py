def count_vowels(word):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_words = ["hello", "world", "python", "programming"]
    for word in sample_words:
        print(f"Number of vowels in '{word}': {count_vowels(word)}")