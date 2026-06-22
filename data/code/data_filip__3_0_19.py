def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in text if char not in vowels])

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Python Programming"
    sample3 = "AeIoUaEiOu"
    print(remove_vowels(sample1))
    print(remove_vowels(sample2))
    print(remove_vowels(sample3))