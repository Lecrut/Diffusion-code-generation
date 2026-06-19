def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample_text_1 = "Alibaba Cloud"
    sample_text_2 = "OpenAI GPT-4"
    sample_text_3 = "Qwen Model"
    sample_text_4 = "AEIOUaeiou"

    result_1 = count_vowels(sample_text_1)
    result_2 = count_vowels(sample_text_2)
    result_3 = count_vowels(sample_text_3)
    result_4 = count_vowels(sample_text_4)

    print(f"'{sample_text_1}': {result_1}")
    print(f"'{sample_text_2}': {result_2}")
    print(f"'{sample_text_3}': {result_3}")
    print(f"'{sample_text_4}': {result_4}")