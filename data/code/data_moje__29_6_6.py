def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
            if char in ('a', 'e', 'i', 'o', 'u'):
                continue
            if char in ('A', 'E', 'I', 'O', 'U'):
                continue
    return count

if __name__ == '__main__':
    test_string = "Hello World"
    result = count_vowels(test_string)
    print(result)