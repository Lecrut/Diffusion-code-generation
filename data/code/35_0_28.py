class VowelCounter:
    VOWELS = "aeiou"

    @staticmethod
    def is_vowel(char):
        return char.lower() in VowelCounter.VOWELS

    def count_vowels(self, input_string):
        count = 0
        for char in input_string:
            if self.is_vowel(char):
                count += 1
        return count

if __name__ == '__main__':
    test_string = "Hello World, this is a test string."
    counter = VowelCounter()
    result = counter.count_vowels(test_string)
    print(result)