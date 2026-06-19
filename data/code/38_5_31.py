class DuplicateFinder:
    def __init__(self):
        self.char_counts = {}
        self.duplicates = set()

    def find_duplicates(self, s):
        for char in s:
            if char in self.char_counts:
                if self.char_counts[char] == 1:
                    self.duplicates.add(char)
            self.char_counts[char] = self.char_counts.get(char, 0) + 1
        return list(self.duplicates)

if __name__ == '__main__':
    finder = DuplicateFinder()
    
    test_string1 = "programming"
    result1 = finder.find_duplicates(test_string1)
    print(f"Input: {test_string1}")
    print(f"Duplicates: {result1}")

    test_string2 = "hello world"
    result2 = finder.find_duplicates(test_string2)
    print(f"Input: {test_string2}")
    print(f"Duplicates: {result2}")

    test_string3 = "abcde"
    result3 = finder.find_duplicates(test_string3)
    print(f"Input: {test_string3}")
    print(f"Duplicates: {result3}")