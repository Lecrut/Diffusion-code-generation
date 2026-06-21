class StringProcessor:
    def __init__(self, strings):
        self.strings = strings

    def get_first_letters(self):
        return [s[0] for s in self.strings if s]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    processor = StringProcessor(sample_values)
    result = processor.get_first_letters()
    print(result)

    more_fruits = ["kiwi", "mango", "papaya", "grape"]
    another_processor = StringProcessor(more_fruits)
    another_result = another_processor.get_first_letters()
    print(another_result)