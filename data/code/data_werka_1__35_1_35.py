class VowelCounter:
    def __init__(self, text):
        self.text = text

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    test_string1 = "Hello World"
    test_string2 = "Programming is Fun"
    test_string3 = "Rhythm"

    counter1 = VowelCounter(test_string1)
    counter2 = VowelCounter(test_string2)
    counter3 = VowelCounter(test_string3)

    print(f"'{test_string1}': {counter1.count_vowels()}")
    print(f"'{test_string2}': {counter2.count_vowels()}")
    print(f"'{test_string3}': {counter3.count_vowels()}")