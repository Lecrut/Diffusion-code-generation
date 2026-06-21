class NonRepeatingCharFinder:

    def __init__(self):
        self.char_count = {}

    def add_char(self, char):
        if char in self.char_count:
            self.char_count[char] += 1
        else:
            self.char_count[char] = 1

    def find_first_non_repeating(self):
        for char in self.char_count:
            if self.char_count[char] == 1:
                return char
        return None
if __name__ == '__main__':
    finder = NonRepeatingCharFinder()
    finder.add_char('s')
    finder.add_char('w')
    finder.add_char('i')
    finder.add_char('s')
    print(finder.find_first_non_repeating())