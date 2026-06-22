def count_vowels(input_string):
    vowels = "aeiou"
    vowel_count = 0
    for character in input_string:
        if character.lower() in vowels:
            vowel_count += 1
    return vowel_count

if __name__ == '__main__':
    sample_text = "Alibaba Cloud is a leading technology company."
    total_vowels = count_vowels(sample_text)
    print(total_vowels)