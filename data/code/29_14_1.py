def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = count_vowels(sample_text)
    print(result)
    sample_text_2 = "Python Programming"
    result_2 = count_vowels(sample_text_2)
    print(result_2)