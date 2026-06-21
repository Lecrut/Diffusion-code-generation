def count_vowels(text: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Programming is an art of solving problems efficiently."
    result = count_vowels(sample_text)
    print(result)