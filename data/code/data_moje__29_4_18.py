def count_vowels(text):
    vowels = set('aeiouAEIOU')
    unique_chars = set(text)
    return len(unique_chars & vowels)

if __name__ == '__main__':
    sample_text = "Hello World"
    print(count_vowels(sample_text))