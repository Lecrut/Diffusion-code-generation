class SubstringGenerator:
    def __init__(self, string):
        self.string = string

    def generate(self):
        n = len(self.string)
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield self.string[i:j]

if __name__ == '__main__':
    test_string = "abc"
    generator = SubstringGenerator(test_string)
    print("Substrings of 'abc':")
    for sub in generator.generate():
        print(sub)

    test_string_long = "abcdefg"
    long_generator = SubstringGenerator(test_string_long)
    print("\nSubstrings of 'abcdefg':")
    for sub in long_generator.generate():
        print(sub)