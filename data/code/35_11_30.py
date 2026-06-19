class VowelCounter:
    def __init__(self, text):
        self.text = text

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Python Programming"
    sample_string_3 = "Rhythm"
    sample_string_4 = "AEIOUaeiou123!"

    counter_1 = VowelCounter(sample_string_1)
    counter_2 = VowelCounter(sample_string_2)
    counter_3 = VowelCounter(sample_string_3)
    counter_4 = VowelCounter(sample_string_4)

    print(f"'{sample_string_1}': {counter_1.count_vowels()}")
    print(f"'{sample_string_2}': {counter_2.count_vowels()}")
    print(f"'{sample_string_3}': {counter_3.count_vowels()}")
    print(f"'{sample_string_4}': {counter_4.count_vowels()}")