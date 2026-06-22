class PunctuationIsolator:
    PUNCTUATIONS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    @staticmethod
    def isolate(sentences):
        return [PunctuationIsolator._isolate(sentence) for sentence in sentences]
    
    @staticmethod
    def _isolate(sentence):
        return ''.join(char if char in PunctuationIsolator.PUNCTUATIONS else ' ' for char in sentence)

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world!",
        "Python is fun.",
        "Is it raining?",
        "No punctuation here"
    ]
    isolated_punctuations = PunctuationIsolator.isolate(sample_sentences)
    print(isolated_punctuations)