class VowelCounter:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def count(self, text: str) -> int:
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    
    sample_texts = [
        "Hello World",
        "Python is great!",
        "aeiouAEIOU",
        "",
        "bcdfg"
    ]
    
    for text in sample_texts:
        print(f"'{text}' -> {counter.count(text)}")