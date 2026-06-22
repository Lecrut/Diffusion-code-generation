class StringCombiner:
    def __init__(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings.")
        self.str1 = str1
        self.str2 = str2

    def combine(self):
        return f"{self.str1} {self.str2}"

if __name__ == '__main__':
    try:
        combiner = StringCombiner("hello", "world")
        result = combiner.combine()
        print(result)
    except ValueError as e:
        print(e)