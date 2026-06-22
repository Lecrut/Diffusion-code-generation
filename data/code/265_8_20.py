class ConsonantReverser:
    VOWELS = 'aeiouAEIOU'
    
    @staticmethod
    def extract_non_vowels_reverse(phrase):
        non_vowels = [char for char in phrase if char not in ConsonantReverser.VOWELS]
        return ''.join(non_vowels[::-1])

if __name__ == '__main__':
    sample_phrase = 'Hello, World!'
    result = ConsonantReverser.extract_non_vowels_reverse(sample_phrase)
    print(result)