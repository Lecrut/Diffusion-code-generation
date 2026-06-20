class VowelFilter:
    VOWELS = frozenset('aeiouAEIOU')

    def __init__(self, text):
        self.text = text

    def filter(self):
        return ''.join(c for c in self.text if c not in self.VOWELS)

    def count_removed(self):
        return sum(1 for c in self.text if c in self.VOWELS)

    def process_and_summarize(self):
        filtered = self.filter()
        removed_count = self.count_removed()
        return filtered, removed_count

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    filter_obj = VowelFilter(sample_text)
    filtered_text, removed_count = filter_obj.process_and_summarize()
    print(filtered_text)
    print(removed_count)