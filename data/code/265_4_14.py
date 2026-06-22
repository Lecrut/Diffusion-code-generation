def extract_vowels_reverse(input_string):
    vowels = "aeiouAEIOU"
    result = [char for char in input_string if char in vowels][::-1]
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello World!"
    reversed_vowels = extract_vowels_reverse(sample_string)
    print(reversed_vowels)