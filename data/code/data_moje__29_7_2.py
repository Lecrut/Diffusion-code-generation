def count_vowels(text: str) -> int:
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    text = "Hello World"
    result = count_vowels(text)
    print(result)