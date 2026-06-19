class RepeatedCharacterFinder:
    def __init__(self, input_string):
        self.input_string = input_string

    @staticmethod
    def count_characters(input_string):
        char_count = {}
        for char in input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

    def find_repeated(self):
        char_count = self.count_characters(self.input_string)
        repeated_chars = [char for char, count in char_count.items() if count > 1]
        return sorted(repeated_chars)

if __name__ == '__main__':
    sample_string = "hello world"
    finder = RepeatedCharacterFinder(sample_string)
    result = finder.find_repeated()
    print(result)