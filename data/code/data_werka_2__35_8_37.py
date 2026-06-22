def count_vowels(input_string):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in input_string if char in vowels)

if __name__ == '__main__':
    sample_input_1 = 'Hello, World!'
    sample_input_2 = 'Alibaba Cloud'
    sample_input_3 = 'Python Programming'
    print(count_vowels(sample_input_1))
    print(count_vowels(sample_input_2))
    print(count_vowels(sample_input_3))