def count_vowels(text):
    vowels = set("aeiou")
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! 123 AEIOU"
    result = count_vowels(sample_string)
    print(result)