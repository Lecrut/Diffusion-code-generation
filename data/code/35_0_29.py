VOWELS = "aeiou"

def count_vowels(input_string):
    return sum(1 for char in input_string if char.lower() in VOWELS)

if __name__ == '__main__':
    test_string = "Alibaba Cloud is an innovative technology company."
    result = count_vowels(test_string)
    print(result)