def count_consonants(s):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    test_string = "Hello, World! 123"
    result = count_consonants(test_string)
    print(result)