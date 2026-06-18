class VowelCounter:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def count(self, text: str) -> int:
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_texts = [
        "Hello World",
        "aeiouAEIOU",
        "",
        "Python Programming"
    ]

    for test_text in sample_texts:
        result = counter.count(test_text)
        print(f"'{test_text}' -> {result} vowels")