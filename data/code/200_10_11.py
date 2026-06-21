class StringFilter:
    def __init__(self, strings):
        self.strings = strings

    def filter_alphabetic(self):
        return [s for s in self.strings if s.isalpha()]

if __name__ == '__main__':
    sample_strings = ["hello", "world!", "Python3", "filter", "123"]
    filter_instance = StringFilter(sample_strings)
    filtered_values = filter_instance.filter_alphabetic()
    print(filtered_values)