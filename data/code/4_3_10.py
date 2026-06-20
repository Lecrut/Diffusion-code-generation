def count_consonants(text):
    vowel_set = set("aeiouAEIOU")
    alpha_chars = [c for c in text if c.isalpha()]
    consonant_list = [c for c in alpha_chars if c not in vowel_set]
    total_count = len(consonant_list)
    return total_count

if __name__ == '__main__':
    sample_input = "Python 3.9 is great!"
    final_result = count_consonants(sample_input)
    print(final_result)