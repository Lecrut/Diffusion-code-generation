def count_vowels(text):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello, World! 123 AEIOU"
    empty_text = ""
    no_vowels_text = "rhythm"
    
    print(count_vowels(sample_text))
    print(count_vowels(empty_text))
    print(count_vowels(no_vowels_text))