def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    sample_text1 = "Hello World! 123"
    sample_text2 = "Programming is Fun, how are you?"
    sample_text3 = "Rhythm myth"
    sample_text4 = "AEIOUaeiou123"
    result1 = count_vowels(sample_text1)
    result2 = count_vowels(sample_text2)
    result3 = count_vowels(sample_text3)
    result4 = count_vowels(sample_text4)
    print(result1)
    print(result2)
    print(result3)
    print(result4)