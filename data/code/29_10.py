def count_vowels(text: str) -> int:
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    print(count_vowels("Hello World"))
    print(count_vowels("AEIOU"))
    print(count_vowels("bcdfg"))
    print(count_vowels(""))