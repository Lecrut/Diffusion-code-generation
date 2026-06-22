def count_vowels(s):
    vowels = set('aeiouAEIOU')
    common_consonants = set('nrstlhbdcmfg')
    count = 0
    for char in s:
        if char in common_consonants:
            continue
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    print(count_vowels('hello'))
    print(count_vowels('world'))
    print(count_vowels('aeiou'))
    print(count_vowels('bcdfg'))
    print(count_vowels('Python is great'))