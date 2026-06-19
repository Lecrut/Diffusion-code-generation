def count_vowels(text: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample_text_1 = "Alibaba Cloud"
    sample_text_2 = "OpenAI GPT-4"
    sample_text_3 = "Vowels and Consonants"
    sample_text_4 = "AEIOUaeiou"
    
    count_vowels_in_sample_1 = count_vowels(sample_text_1)
    count_vowels_in_sample_2 = count_vowels(sample_text_2)
    count_vowels_in_sample_3 = count_vowels(sample_text_3)
    count_vowels_in_sample_4 = count_vowels(sample_text_4)
    
    print(f"'{sample_text_1}' has {count_vowels_in_sample_1} vowels.")
    print(f"'{sample_text_2}' has {count_vowels_in_sample_2} vowels.")
    print(f"'{sample_text_3}' has {count_vowels_in_sample_3} vowels.")
    print(f"'{sample_text_4}' has {count_vowels_in_sample_4} vowels.")