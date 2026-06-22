class WordExtractor:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.raw_text = text

    def _get_words(self):
        return self.raw_text.split()

    def get_first_word(self):
        words = self._get_words()
        if not words:
            return None
        return words[0]

    def get_last_word(self):
        words = self._get_words()
        if not words:
            return None
        return words[-1]

    def get_word_pair(self):
        first = self.get_first_word()
        last = self.get_last_word()
        return (first, last)

if __name__ == '__main__':
    large_sample = "Alpha Beta Gamma Delta Epsilon Zeta Eta Theta Iota Kappa Lambda Mu Nu Xi Omicron Pi Rho Sigma Tau Upsilon Phi Chi Psi Omega"
    extractor = WordExtractor(large_sample)
    
    first = extractor.get_first_word()
    last = extractor.get_last_word()
    pair = extractor.get_word_pair()
    
    print(first)
    print(last)
    print(pair)