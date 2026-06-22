def count_vowels(text):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    count = 0
    for char in text:
        if char in vowels:
            count += 1
        elif char in consonants:
            continue
    return count

if __name__ == '__main__':
    samples = ['hello', 'world', 'AEIOU', 'xyz', 'a', '', 'b', 'aei', 'bcd', 'AEae']
    for sample in samples:
        result = count_vowels(sample)
        print(result)