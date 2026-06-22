class CharacterCounter:
    def __init__(self):
        self.char_count = {}

    def count_characters(self, s):
        for char in s:
            if char in self.char_count:
                self.char_count[char] += 1
            else:
                self.char_count[char] = 1

    def get_counts(self):
        return self.char_count

if __name__ == '__main__':
    counter = CharacterCounter()
    sample_string = "hello world"
    counter.count_characters(sample_string)
    print(counter.get_counts())