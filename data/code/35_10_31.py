class VowelCounter:
    def __init__(self):
        self.vowels = "aeiou"

    def is_vowel(self, char):
        return char.lower() in self.vowels

    def count(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        count = 0
        for char in text:
            if self.is_vowel(char):
                count += 1
        return count

if __name__ == '__main__':
    test_string_1 = "Hello World"
    counter = VowelCounter()
    result_1 = counter.count(test_string_1)
    print(result_1)

    test_string_2 = "Programming is Fun"
    result_2 = counter.count(test_string_2)
    print(result_2)

    test_string_3 = "AEIOUaeiou"
    result_3 = counter.count(test_string_3)
    print(result_3)