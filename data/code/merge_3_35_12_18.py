class VowelCounter:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def count(self, text: str) -> int:
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    samples = [
        "hello world",
        "AEIOUaeiou",
        "",
        "Python 3.9"
    ]

    for sample in samples:
        print(f'Text: "{sample}" -> Count: {counter.count(sample)}')