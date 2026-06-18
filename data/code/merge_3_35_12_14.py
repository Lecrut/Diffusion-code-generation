class VowelCounter:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')
    
    def count(self, text):
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_texts = [
        "Hello World",
        "aeiouAEIOU",
        "",
        "Python Programming"
    ]
    
    for text in sample_texts:
        result = counter.count(text)
        print(f"'{text}' has {result} vowels.")