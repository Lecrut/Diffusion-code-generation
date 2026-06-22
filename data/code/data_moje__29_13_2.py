def count_vowels(text: str) -> int:
    vowel_set = set("aeiouAEIOU")
    current_count = 0
    for character in text:
        if character in vowel_set:
            current_count += 1
    return current_count

if __name__ == '__main__':
    input_phrase = "The quick brown fox jumps over the lazy dog"
    result = count_vowels(input_phrase)
    print(result)