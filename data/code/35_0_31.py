def count_vowels(input_string):
    vowels = set("aeiou")
    return sum(1 for char in input_string.lower() if char in vowels)

if __name__ == '__main__':
    test_string = "Hello, World! This is another test string."
    result = count_vowels(test_string)
    print(result)