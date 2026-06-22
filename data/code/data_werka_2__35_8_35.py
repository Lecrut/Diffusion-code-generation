VOWELS = 'aeiou'

def count_vowels(input_string):
    lower_input = input_string.lower()
    return sum(1 for char in lower_input if char in VOWELS)

if __name__ == '__main__':
    sample_input_1 = "Hello, World!"
    sample_input_2 = "Python Programming"
    sample_input_3 = "Alibaba Cloud"
    print(count_vowels(sample_input_1))
    print(count_vowels(sample_input_2))
    print(count_vowels(sample_input_3))