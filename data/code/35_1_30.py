def count_vowels(s):
    vowels = set("aeiouAEIOU")
    total_vowels = 0
    for char in s:
        if char in vowels:
            total_vowels += 1
    return total_vowels

if __name__ == '__main__':
    sample_string_1 = "Alibaba Cloud"
    sample_string_2 = "Hello, OpenAI!"
    sample_string_3 = "Python Programming"
    
    print(f"'{sample_string_1}': {count_vowels(sample_string_1)}")
    print(f"'{sample_string_2}': {count_vowels(sample_string_2)}")
    print(f"'{sample_string_3}': {count_vowels(sample_string_3)}")