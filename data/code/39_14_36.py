class SubstringGenerator:

    def __init__(self, s):
        self.s = s

    def generate(self):
        n = len(self.s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield self.s[i:j]
if __name__ == '__main__':
    sample_string_1 = 'abc'
    generator_1 = SubstringGenerator(sample_string_1)
    for substring in generator_1.generate():
        print(substring)
    sample_string_2 = 'xyz'
    generator_2 = SubstringGenerator(sample_string_2)
    all_substrings_2 = list(generator_2.generate())
    print(all_substrings_2)
    sample_string_3 = 'hello'
    generator_3 = SubstringGenerator(sample_string_3)
    all_substrings_3 = list(generator_3.generate())
    print(all_substrings_3[:5])