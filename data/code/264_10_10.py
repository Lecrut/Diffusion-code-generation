class WordFrequency:
    def __init__(self):
        self.frequency = {}

    @staticmethod
    def process_text(text):
        return text.lower().split()

    def update_frequency(self, words):
        for word in words:
            if word in self.frequency:
                self.frequency[word] += 1
            else:
                self.frequency[word] = 1

    def get_frequency(self):
        return self.frequency

if __name__ == '__main__':
    sample_text = "Hello world hello Python python"
    wf = WordFrequency()
    words = wf.process_text(sample_text)
    wf.update_frequency(words)
    result = wf.get_frequency()
    print(result)