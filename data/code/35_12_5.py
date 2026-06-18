class VowelCounter:
    def count(self, text):
        vowels = set("aeiouAEIOU")
        return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    sample_texts = [
        "Hello World",
        "Python Programming 2024",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]

    counter = VowelCounter()
    
    for text in sample_texts:
        count = counter.count(text)
        print(f"'{text}' contains {count} vowels.")