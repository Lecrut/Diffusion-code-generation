def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for c in s if c in vowels)

if __name__ == '__main__':
    sample = "Hello World"
    print(count_vowels(sample))