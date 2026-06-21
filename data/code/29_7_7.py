def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello World! How Are You?"
    result = count_vowels(sample_string)
    print(result)