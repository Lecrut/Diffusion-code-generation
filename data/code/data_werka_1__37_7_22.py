class StringCombiner:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def combine(self):
        if not isinstance(self.str1, str) or not isinstance(self.str2, str):
            raise ValueError("Both inputs must be strings.")
        return f"{self.str1} {self.str2}"

if __name__ == '__main__':
    try:
        string_combiner = StringCombiner("Hello", "World")
        result = string_combiner.combine()
        print(result)
    except ValueError as e:
        print(e)