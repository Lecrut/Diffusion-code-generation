def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    sample_string1 = 'Hello, World!'
    sample_string2 = 'Python Programming'
    print(count_vowels(sample_string1))
    print(count_vowels(sample_string2))