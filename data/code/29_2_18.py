def count_vowels(text):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    text1 = "Hello World"
    text2 = "Python Programming"
    text3 = ""
    text4 = "rhythm"

    print(count_vowels(text1))
    print(count_vowels(text2))
    print(count_vowels(text3))
    print(count_vowels(text4))