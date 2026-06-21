VOWEL_SET = frozenset({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})

def count_vowels(text):
    total = 0
    for character in text:
        if character in VOWEL_SET:
            total += 1
    return total

if __name__ == '__main__':
    sample_input = 'Supercalifragilisticexpialidocious has many vowels.'
    calculated_count = count_vowels(sample_input)
    print(calculated_count)