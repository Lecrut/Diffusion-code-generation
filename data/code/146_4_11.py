class NonRepeatingCharFinder:
    def __init__(self):
        self.char_count = {}

    def add_char(self, char):
        if char in self.char_count:
            self.char_count[char] += 1
        else:
            self.char_count[char] = 1

    def find_non_repeating(self, s):
        for char in s:
            if self.char_count[char] == 1:
                return char
        return None

if __name__ == '__main__':
    finder = NonRepeatingCharFinder()
    print(finder.find_non_repeating("swiss"))