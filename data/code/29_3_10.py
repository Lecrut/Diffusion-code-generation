def count_vowels(strings):
    return sum([1 for s in strings for c in s.lower() if c in 'aeiou'])

if __name__ == '__main__':
    sample_strings = ['hello', 'world', 'python', 'programming']
    result = count_vowels(sample_strings)
    print(result)