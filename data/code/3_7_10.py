def remove_vowels(text):
    vowel_set = set('aeiouAEIOU')
    filtered_chars = [ch for ch in text if ch not in vowel_set]
    result_string = ''.join(filtered_chars)
    return result_string

if __name__ == '__main__':
    test_input = "Education is the most powerful weapon."
    cleaned_output = remove_vowels(test_input)
    print(cleaned_output)