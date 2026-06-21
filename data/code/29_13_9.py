def count_vowels(text: str) -> int:
    return sum(1 for char in text.lower() if char in "aeiou")

if __name__ == '__main__':
    text = "Hello World"
    result = count_vowels(text)
    print(result)