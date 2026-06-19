VOWELS = "aeiou"

def count_vowels(input_string):
    def is_vowel(char):
        return char.lower() in VOWELS

    return sum(is_vowel(char) for char in input_string)

if __name__ == '__main__':
    test_string1 = "Hello World, this is a test string."
    test_string2 = "Programming is Awesome"
    result1 = count_vowels(test_string1)
    result2 = count_vowels(test_string2)
    print(result1)
    print(result2)