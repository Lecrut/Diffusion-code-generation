VOWELS = set('aeiouAEIOU')

def count_vowels(input_string):
    return sum(1 for char in input_string if char in VOWELS)

if __name__ == '__main__':
    sample_input = "Hello, World!"
    print(count_vowels(sample_input))