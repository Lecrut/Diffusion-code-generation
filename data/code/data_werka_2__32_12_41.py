class CharacterCounter:
    def __init__(self, text):
        self.text = text

    def count_characters(self):
        return len(self.text)

if __name__ == '__main__':
    sample_text1 = "Hello, World!"
    sample_text2 = "Python"
    sample_text3 = "OpenAI"
    sample_text4 = ""
    sample_text5 = "1234567890"

    counter1 = CharacterCounter(sample_text1)
    counter2 = CharacterCounter(sample_text2)
    counter3 = CharacterCounter(sample_text3)
    counter4 = CharacterCounter(sample_text4)
    counter5 = CharacterCounter(sample_text5)

    print(counter1.count_characters())
    print(counter2.count_characters())
    print(counter3.count_characters())
    print(counter4.count_characters())
    print(counter5.count_characters())