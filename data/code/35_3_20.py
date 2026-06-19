def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

if __name__ == '__main__':
    sample_string = "Hello World"
    print(count_vowels(sample_string))