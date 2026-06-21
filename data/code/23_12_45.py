class StringComparer:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def validate_inputs(self):
        if not isinstance(self.str1, str) or not isinstance(self.str2, str):
            raise ValueError("Both inputs must be strings")

    def compare(self):
        self.validate_inputs()
        return (self.str1 > self.str2) - (self.str1 < self.str2)

if __name__ == '__main__':
    comparer = StringComparer("kiwi", "mango")
    result = comparer.compare()
    print(result)