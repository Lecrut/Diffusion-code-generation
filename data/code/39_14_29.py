class SubstringGenerator:
    @staticmethod
    def generate_substrings(s):
        n = len(s)
        for i in range(n):
            for j in range(i, n + 1):
                yield s[i:j]

if __name__ == '__main__':
    sample_string_1 = "abc"
    generator_1 = SubstringGenerator.generate_substrings(sample_string_1)
    print(list(generator_1))

    sample_string_2 = "a"
    generator_2 = SubstringGenerator.generate_substrings(sample_string_2)
    print(list(generator_2))

    sample_string_3 = "ab"
    generator_3 = SubstringGenerator.generate_substrings(sample_string_3)
    print(list(generator_3))