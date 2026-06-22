import re

class WordGrouping:
    def __init__(self):
        self.groups = {}
    
    def group_words(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        for word in words:
            first_letter = word[0]
            if first_letter not in self.groups:
                self.groups[first_letter] = []
            self.groups[first_letter].append(word)
    
    def get_groups(self):
        return self.groups

if __name__ == '__main__':
    sample_text = "Hello world, this is a test. This text is for testing."
    word_grouping = WordGrouping()
    word_grouping.group_words(sample_text)
    print(word_grouping.get_groups())