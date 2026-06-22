def count_vowels(s):
    count = 0
    vowels = set('aeiouAEIOU')
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello World"
    result = count_vowels(sample_string)
    print(result)