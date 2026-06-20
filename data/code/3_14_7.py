import re

REMOVED_VOWELS = re.compile(r'[aeiouAEIOU]')

def remove_vowels(text):
    return REMOVED_VOWELS.sub('', text)

if __name__ == '__main__':
    sample_input = "Hello World"
    result = remove_vowels(sample_input)
    print(result)
    
    sample_input_2 = "Programming is fun"
    result_2 = remove_vowels(sample_input_2)
    print(result_2)