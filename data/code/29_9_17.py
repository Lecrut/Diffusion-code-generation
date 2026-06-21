import string

def count_vowels(text: str) -> int:
    translation_table = str.maketrans('', '', string.ascii_lowercase + string.ascii_uppercase)
    vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in text:
        if char in vowel_set:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "A quick brown fox jumps over the lazy dog and the eagle flew high in the sky above the ocean"
    result = count_vowels(sample_text)
    print(result)