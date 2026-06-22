VOWELS = 'aeiouAEIOU'

def extract_vowels_reverse(input_string):
    vowels = [char for char in input_string if char in VOWELS]
    return ''.join(vowels[::-1])

if __name__ == '__main__':
    sample_string = "Hello World!"
    result = extract_vowels_reverse(sample_string)
    print(result)