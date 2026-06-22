VOWELS = set('aeiouAEIOU')

def count_vowels(word):
    return sum(1 for char in word if char in VOWELS)

if __name__ == '__main__':
    sample_word = "Qwen, the AI assistant"
    print(count_vowels(sample_word))