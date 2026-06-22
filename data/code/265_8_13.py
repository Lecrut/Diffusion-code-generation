class ConsonantHandler:
    def __init__(self):
        self.vowels = 'aeiouAEIOU'
    
    def filter_and_reverse(self, phrase):
        consonants = [char for char in phrase if char not in self.vowels]
        return ''.join(consonants[::-1])

if __name__ == '__main__':
    handler = ConsonantHandler()
    sample_phrase = 'Hello, World!'
    result = handler.filter_and_reverse(sample_phrase)
    print(result)