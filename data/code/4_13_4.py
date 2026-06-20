def count_consonants(text: str) -> int:
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char.isalpha() and char not in vowels)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_consonants(sample_text)
    print(result)