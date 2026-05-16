def count_vowels(string_list):
    result_dict = {}
    vowels = "aeiouAEIOU"
    for s in string_list:
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        result_dict[s] = count
    return result_dict
if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "programming", "aeiou"]
    vowel_counts = count_vowels(sample_list)
    print(vowel_counts)