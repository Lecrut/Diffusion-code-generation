import string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
if __name__ == '__main__':
    test_string = "Hello World, this is a test string."
    result = count_vowels(test_string)
    print(result)