def count_vowels(text: str) -> int:
    vowel_set = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char in vowel_set:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = ['Hello World', 'Python Programming', 'AEIOU', 'bcdfg']
    for s in sample_strings:
        result = count_vowels(s)
        print(result)