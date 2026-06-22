def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

if __name__ == '__main__':
    test_string = "Programming is fun and efficient"
    result = count_vowels(test_string)
    print(result)