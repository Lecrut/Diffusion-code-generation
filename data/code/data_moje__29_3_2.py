def count_vowels(strings):
    vowels = set('aeiouAEIOU')
    return sum([1 for s in strings for c in s if c in vowels])

if __name__ == '__main__':
    sample_strings = ['hello', 'world', 'python', 'vowels']
    print(count_vowels(sample_strings))