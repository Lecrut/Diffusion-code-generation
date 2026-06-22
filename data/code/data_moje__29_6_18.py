def count_vowels(s):
    vowels = 0
    for char in s:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowels += 1
        elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
            vowels += 1
    return vowels

if __name__ == '__main__':
    test_string = "Hello World"
    result = count_vowels(test_string)
    print(result)