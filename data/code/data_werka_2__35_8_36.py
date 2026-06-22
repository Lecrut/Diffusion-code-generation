def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

if __name__ == '__main__':
    sample_input = "OpenAI"
    result = count_vowels(sample_input)
    print(result)