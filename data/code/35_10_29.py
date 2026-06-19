class VowelCounter:
    def __init__(self):
        self.vowels = "aeiou"

    def count(self, text):
        vowel_count = 0
        for char in text:
            if char.lower() in self.vowels:
                vowel_count += 1
        return vowel_count

if __name__ == '__main__':
    sample_text_1 = "Alibaba Cloud is Awesome"
    counter = VowelCounter()
    result_1 = counter.count(sample_text_1)
    print(result_1)

    sample_text_2 = "OpenAI and Alibaba are leading in AI"
    result_2 = counter.count(sample_text_2)
    print(result_2)

    sample_text_3 = "AEIOUaeiou"
    result_3 = counter.count(sample_text_3)
    print(result_3)