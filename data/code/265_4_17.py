def extract_vowels_and_reverse(input_string):
    vowels = "aeiouAEIOU"
    extracted_chars = [char for char in input_string if char in vowels]
    return ''.join(extracted_chars[::-1])

if __name__ == '__main__':
    test_phrase = "Programming is fun!"
    result = extract_vowels_and_reverse(test_phrase)
    print(result)