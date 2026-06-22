class VowelCounter:
    def __init__(self, text):
        self.text = text

    def count_vowels(self):
        vowels_map = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for char in self.text.lower():
            if char in vowels_map:
                vowels_map[char] += 1
        return sum(vowels_map.values())

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    counter = VowelCounter(sample_string)
    vowel_count = counter.count_vowels()
    print(vowel_count)