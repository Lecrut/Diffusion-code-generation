class PhraseLengthCalculator:
    MAX_CACHE_SIZE = 10

    def __init__(self):
        self.cache = {}

    @staticmethod
    def _calculate_length(phrase):
        return len(phrase)

    def calculate_phrase_length(self, phrase):
        if not isinstance(phrase, str):
            raise ValueError("Input must be a string")
        
        if phrase in self.cache:
            return self.cache[phrase]
        
        length = self._calculate_length(phrase)
        if len(self.cache) >= PhraseLengthCalculator.MAX_CACHE_SIZE:
            self.cache.pop(next(iter(self.cache)))
        self.cache[phrase] = length
        
        return length

if __name__ == '__main__':
    calculator = PhraseLengthCalculator()
    sample_phrases = ["Hello, World!", "Optimized function", "", "Python programming"]
    for phrase in sample_phrases:
        print(calculator.calculate_phrase_length(phrase))