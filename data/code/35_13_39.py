def count_vowels(word):
    vowels = frozenset('aeiouAEIOU')
    return sum(1 for char in word if char in vowels)

if __name__ == '__main__':
    sample_word = "Qwen, the AI assistant"
    print(count_vowels(sample_word))