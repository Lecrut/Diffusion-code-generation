class CharacterFrequency:
    def __init__(self):
        self.char_count = {}

    def count_chars(self, phrase):
        for char in phrase:
            if char in self.char_count:
                self.char_count[char] += 1
            else:
                self.char_count[char] = 1

    def get_most_frequent_chars(self):
        max_count = max(self.char_count.values(), default=0)
        return [char for char, count in self.char_count.items() if count == max_count]

if __name__ == '__main__':
    cf = CharacterFrequency()
    sample_phrase = "hello world"
    cf.count_chars(sample_phrase)
    print(cf.get_most_frequent_chars())