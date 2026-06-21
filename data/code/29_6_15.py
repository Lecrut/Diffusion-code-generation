def count_vowels(text):
    vowels = set('aeiouAEIOU')
    common_consonants = set('ntsrllntrslne')
    count = 0
    for char in text:
        if char in common_consonants:
            continue
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample1 = "hello"
    sample2 = "rhythm"
    sample3 = "education"
    sample4 = ""
    sample5 = "AEIOU"

    print(count_vowels(sample1))
    print(count_vowels(sample2))
    print(count_vowels(sample3))
    print(count_vowels(sample4))
    print(count_vowels(sample5))