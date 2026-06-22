def count_consonants(text):
    if not isinstance(text, str):
        return 0
    vowels = set('aeiouAEIOU')
    alpha_chars = [c for c in text if c.isalpha()]
    return sum(1 for c in alpha_chars if c not in vowels)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_consonants(sample_text)
    print(result)