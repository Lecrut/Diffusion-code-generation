def count_vowels(text):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    print(count_vowels("Hello World"))
    print(count_vowels("Python Programming"))
    print(count_vowels("AEIOU aeiou"))
    print(count_vowels("Rhythm"))
    print(count_vowels(""))