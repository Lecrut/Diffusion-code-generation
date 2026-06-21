class NonRepeatingCharFinder:
    def __init__(self):
        self.char_count = {}

    def find_first_non_repeating(self, s):
        for char in s:
            if char in self.char_count:
                self.char_count[char] += 1
            else:
                self.char_count[char] = 1
        
        for char in s:
            if self.char_count[char] == 1:
                return char
        return None

if __name__ == '__main__':
    finder = NonRepeatingCharFinder()
    print(finder.find_first_non_repeating("swiss"))
    print(finder.find_first_non_repeating("programming"))
    print(finder.find_first_non_repeating("aabbccddeeffg"))