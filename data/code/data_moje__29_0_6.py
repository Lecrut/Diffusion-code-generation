def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Programming is fun and efficient"
    result = count_vowels(sample_text)
    print(result)