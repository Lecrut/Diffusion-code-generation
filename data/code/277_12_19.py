class VowelCounter:
    def __init__(self):
        self.vowels = set("aeiou")

    def count_vowels(self, text):
        vowel_count = 0
        for char in text.lower():
            if char in self.vowels:
                vowel_count += 1
        return vowel_count

if __name__ == '__main__':
    counter = VowelCounter()
    
    sample_string_1 = "Hello World"
    result_1 = counter.count_vowels(sample_string_1)
    print(f"The string: '{sample_string_1}' has {result_1} vowels.")
    
    sample_string_2 = "Programming is Fun"
    result_2 = counter.count_vowels(sample_string_2)
    print(f"The string: '{sample_string_2}' has {result_2} vowels.")
    
    sample_string_3 = "AEIOUaeiou"
    result_3 = counter.count_vowels(sample_string_3)
    print(f"The string: '{sample_string_3}' has {result_3} vowels.")