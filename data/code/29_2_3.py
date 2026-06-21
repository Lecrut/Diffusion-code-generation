def count_vowels(text: str) -> int:
    if not text:
        return 0
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    result = count_vowels("Hello World")
    print(result)
    result2 = count_vowels("")
    print(result2)
    result3 = count_vowels("12345")
    print(result3)
    result4 = count_vowels("AEIOUaeiou")
    print(result4)