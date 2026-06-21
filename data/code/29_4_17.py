def count_vowels(text: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    unique_chars = set(text)
    found_vowels = unique_chars.intersection(vowels)
    total = 0
    for char in text:
        if char in found_vowels:
            total += 1
    return total

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_vowels(sample_text)
    print(result)