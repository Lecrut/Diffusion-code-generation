class StringCombiner:
    def __init__(self):
        self.separator = ""

    def combine(self, str1, str2):
        combined_string = ''.join([str1, self.separator, str2])
        return combined_string

if __name__ == '__main__':
    combiner = StringCombiner()
    first_part = "Good morning"
    second_part = "Beautiful world"
    result = combiner.combine(first_part, second_part)
    print(result)