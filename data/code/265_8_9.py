class NonVowelReverser:
    def __init__(self):
        self.vowels = 'aeiouAEIOU'
    
    def extract_non_vowels_reverse(self, phrase):
        non_vowels = [char for char in phrase if char not in self.vowels]
        return ''.join(non_vowels[::-1])

if __name__ == '__main__':
    reverser = NonVowelReverser()
    sample_phrase = 'Hello, World!'
    result = reverser.extract_non_vowels_reverse(sample_phrase)
    print(result)