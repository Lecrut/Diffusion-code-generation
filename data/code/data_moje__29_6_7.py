def count_vowels(s):
    count = 0
    vowel_set = frozenset('aeiouAEIOU')
    for char in s:
        if char in vowel_set:
            count += 1
    return count

if __name__ == '__main__':
    text = 'Hello World'
    result = count_vowels(text)
    print(result)