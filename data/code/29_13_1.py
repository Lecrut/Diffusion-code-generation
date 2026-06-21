def count_vowels(text: str) -> int:
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample_text = "Hello World"
    print(count_vowels(sample_text))