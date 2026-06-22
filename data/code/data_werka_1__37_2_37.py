class StringCombiner:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def combine(self):
        return self.str1 + self.str2

    def get_combined_length(self):
        combined = self.combine()
        return len(combined)

if __name__ == '__main__':
    combiner_instance = StringCombiner("Hello, ", "World!")
    result = combiner_instance.combine()
    print(result)
    length_result = combiner_instance.get_combined_length()
    print(length_result)