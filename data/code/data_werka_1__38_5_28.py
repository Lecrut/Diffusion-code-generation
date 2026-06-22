class CharCounter:
    def __init__(self):
        self.char_counts = {}
    
    def count_characters(self, s):
        for char in s:
            if char in self.char_counts:
                self.char_counts[char] += 1
            else:
                self.char_counts[char] = 1
    
    def find_duplicates(self):
        duplicates = set()
        for char, count in self.char_counts.items():
            if count > 1:
                duplicates.add(char)
        return list(duplicates)

if __name__ == '__main__':
    test_string1 = "programming"
    counter1 = CharCounter()
    counter1.count_characters(test_string1)
    result1 = counter1.find_duplicates()
    print(f"String: {test_string1}, Duplicates: {result1}")

    test_string2 = "hello world"
    counter2 = CharCounter()
    counter2.count_characters(test_string2)
    result2 = counter2.find_duplicates()
    print(f"String: {test_string2}, Duplicates: {result2}")

    test_string3 = "abcde"
    counter3 = CharCounter()
    counter3.count_characters(test_string3)
    result3 = counter3.find_duplicates()
    print(f"String: {test_string3}, Duplicates: {result3}")