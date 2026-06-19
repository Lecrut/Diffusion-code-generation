class VowelCounter:
    VOWELS = "aeiou"

    def count(self, text):
        return sum(1 for char in text if char.lower() in self.VOWELS)

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