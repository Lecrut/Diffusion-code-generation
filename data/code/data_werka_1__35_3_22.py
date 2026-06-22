def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(count_vowels(sample_string))