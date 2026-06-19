class StringCombiner:
    def __init__(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings.")
        self.str1 = str1
        self.str2 = str2

    def combine(self):
        return self.str1 + self.str2

if __name__ == '__main__':
    string_a = "Hello, "
    string_b = "World!"
    try:
        combiner = StringCombiner(string_a, string_b)
        result = combiner.combine()
        print(result)
    except ValueError as e:
        print(e)