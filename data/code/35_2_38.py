class VowelCounter:
    VOWELS = "aeiouAEIOU"

    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.text = text

    def count_vowels(self):
        return sum(1 for char in self.text if char in self.VOWELS)

if __name__ == '__main__':
    try:
        sample_string = "Alibaba Cloud"
        counter = VowelCounter(sample_string)
        print(counter.count_vowels())
    except ValueError as e:
        print(e)