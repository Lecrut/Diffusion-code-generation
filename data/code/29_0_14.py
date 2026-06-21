def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for c in s if c in vowels)

if __name__ == '__main__':
    print(count_vowels("hello world"))
    print(count_vowels("AEIOU aeio"))
    print(count_vowels("xyz"))
    print(count_vowels(""))