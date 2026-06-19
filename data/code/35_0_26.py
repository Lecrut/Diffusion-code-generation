def count_vowels(input_string):
    vowels = set("aeiou")
    lowercased_string = input_string.lower()
    vowel_count = sum(1 for char in lowercased_string if char in vowels)
    return vowel_count

if __name__ == '__main__':
    sample_text = "Counting the number of vowels in this sentence."
    total_vowels = count_vowels(sample_text)
    print(total_vowels)