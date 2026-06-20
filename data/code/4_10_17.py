def count_consonants(text):
    vowel_set = set("aeiou")
    consonant_total = 0
    for current_char in text:
        lowercase_char = current_char.lower()
        is_alpha = lowercase_char.isalpha()
        is_not_vowel = lowercase_char not in vowel_set
        if is_alpha and is_not_vowel:
            consonant_total += 1
    return consonant_total

if __name__ == '__main__':
    test_input = "Rhythm! 789"
    final_count = count_consonants(test_input)
    print(final_count)