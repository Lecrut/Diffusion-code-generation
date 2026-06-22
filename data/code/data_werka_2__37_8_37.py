class StringCombiner:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    @staticmethod
    def combine_strings(str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both arguments must be strings.")
        return str1 + str2

    def get_combined_result(self):
        return StringCombiner.combine_strings(self.str1, self.str2)

if __name__ == '__main__':
    combiner1 = StringCombiner("Hello, ", "World!")
    print(combiner1.get_combined_result())

    combiner2 = StringCombiner("Python", "Programming")
    print(combiner2.get_combined_result())