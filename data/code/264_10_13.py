class WordFrequency:
    def __init__(self):
        self.frequency = {}

    def update_frequency(self, text):
        words = text.lower().split()
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
    wf.update_frequency(sample_text)
    print(wf.get_frequency())