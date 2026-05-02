import sys
def count_vowels(input_string):
    vowels = "aeiou"
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    return count
if __name__ == '__main__':
    sample_string = "Hello World! This is a Test String."
    result = count_vowels(sample_string)
    print(result)