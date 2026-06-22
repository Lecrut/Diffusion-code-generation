def count_vowels(text):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    empty_string = ""
    result1 = count_vowels(sample_string)
    result2 = count_vowels(empty_string)
    print(result1)
    print(result2)