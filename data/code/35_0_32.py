class VowelCounter:
    VOWELS = "aeiou"

    @staticmethod
    def count_vowels(input_string):
        count = 0
        for char in input_string:
            if char.lower() in VowelCounter.VOWELS:
                count += 1
        return count

if __name__ == '__main__':
    test_string = "Hello World, this is a unique test string."
    result = VowelCounter.count_vowels(test_string)
    print(result)