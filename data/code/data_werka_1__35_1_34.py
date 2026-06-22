def count_vowels(s):
    vowels = "aeiouAEIOU"
    total_vowels = 0
    for char in s:
        if char in vowels:
            total_vowels += 1
    return total_vowels

if __name__ == '__main__':
    sample_text_1 = "Alibaba Cloud"
    sample_text_2 = "Python Programming"
    sample_text_3 = "Qwen AI Model"
    print(f"'{sample_text_1}': {count_vowels(sample_text_1)}")
    print(f"'{sample_text_2}': {count_vowels(sample_text_2)}")
    print(f"'{sample_text_3}': {count_vowels(sample_text_3)}")