class VowelCounter:
    def __init__(self, text):
        self.text = text

    def count_vowels(self):
        vowels_map = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
                     'A': True, 'E': True, 'I': True, 'O': True, 'U': True}
        return sum(vowels_map.get(char, False) for char in self.text)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    counter = VowelCounter(sample_string)
    vowel_count = counter.count_vowels()
    print(vowel_count)