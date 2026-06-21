class WordGenerator:
    def __init__(self, text):
        self.text = text.split()
    
    def __iter__(self):
        for word in self.text:
            cleaned_word = word.strip('.,!?;:"\'()[]{}')
            if cleaned_word:
                yield cleaned_word

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    generator_instance = WordGenerator(sample_string)
    for word in generator_instance:
        print(word)